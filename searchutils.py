import logging
import json
import sys
import os
import re
from sys import platform as _platform
import random
import textwrap
from search import loadpickle, Search, ParseKorpJson, GetMetadata, ParseMatchList, MatchFilter, Condition, FailedKorp, Bar, SerializeMonoMatchList
from deptypetools import makeSearch
from menus import multimenu
from dbmodule import psycopg, mydatabase


class MultiLike():
    """Perform queries with multiple like values"""
    def __init__(self, colname, vals, prefix="",postfix="", exp="LIKE"):
        self.likestring = "(" 
        self.sqlrefs = dict()
        for idx, val in enumerate(vals):
            if self.likestring != "(":
                self.likestring += " OR "
            sqlref = "likef{}".format(idx)
            self.likestring += "{} {} %({})s".format(colname, exp, sqlref)
            self.sqlrefs[sqlref] = prefix + val + postfix
        self.likestring += ")"

def StartLogger(fname = "datascripts.log"):
    """Start a logger"""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(message)s')

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    fh = logging.FileHandler(fname)
    fh.setLevel(logging.DEBUG)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    root.addHandler(fh)
    root.addHandler(ch)
    logging.info('='*50)
    logging.info('='*50)
    logging.info('Started...')
    logging.info('='*50)
    logging.info('='*50)

class SearchController():
    """Control what's being done"""
    def __init__(self, nouncount=None):
        """Start loggers, get connections etc"""
        StartLogger()
        self.cons = {'fi':dict(),'ru':dict()}
        self.cons['fi']['db'] = psycopg('tb_fi','juho')
        self.cons['ru']['db'] = psycopg('tb_ru2','juho')
        self.cons['fi']['table'] = "fi_conll"
        self.cons['ru']['table'] = "ru_conll"
        logging.info("Connections established.")
        self.nouns = {'fi':0,'ru':0}
        if not nouncount:
            self.CountNouns()
        else:
            self.nouns['fi'] = nouncount['fi']
            self.nouns['ru'] = nouncount['ru']
        self.results = dict()
        self.searches = list()

    def ResetCons(self):

        print('\n\nRESETTING the db connections, this is a standard procedure...\n\n')

        del self.cons['fi']['db']
        del self.cons['ru']['db']

        self.cons['fi']['db'] = psycopg('tb_fi','juho')
        self.cons['ru']['db'] = psycopg('tb_ru2','juho')

    def Search(self, lang, cond, headcond=None, finheaddepcond=None, depcond2=None, headdepcond=None,prevcond=None,nextcond=None,secondnextcond=None,prevornext=False,samesentencecond=None, secondpreviouscond=None, limited=None, broad=False):
        con = self.cons[lang]['db']

        thisSearch = Search(con = con)
        thisSearch.queried_table = self.cons[lang]['table']
        thisSearch.isparallel = False
        thisSearch.toplevel = "sentence_id"
        thisSearch.limited = False
        thisSearch.ConditionColumns.append(cond)
        thisSearch.broad = broad
        thisSearch.non_db_data = None

        thisSearch.headcond = headcond
        thisSearch.secondpreviouscond = secondpreviouscond
        thisSearch.prevcond = prevcond
        thisSearch.nextcond=nextcond
        if prevornext:
            #In situations where it is enough for either of the surrounding words to fulfill a criterion
            thisSearch.prevornext['ison'] = True
        thisSearch.samesentencecond = samesentencecond
        thisSearch.secondnextcond = secondnextcond
        thisSearch.headdepcond = headdepcond
        thisSearch.finheaddepcond = finheaddepcond
        thisSearch.depcond2 = depcond2

        thisSearch.Run(False)

        self.searches.append(thisSearch)

        #Store the results in a more comfortable way
        SimplifyResultSet(thisSearch)

        logging.info(thisSearch.absolutematchcount)

        self.searches.append(thisSearch)

        return thisSearch

    def CountNouns(self):
        """Number of nouns from the db"""
        logging.info("counting nouns...")

        nounres = self.cons['ru']['db'].FetchQuery("SELECT count(*) FROM ru_conll WHERE pos IN ('NOUN','P') OR lemma IN ('утром','днём','днем','вечером', 'зимой','летом','весной','осенью','ночью')")
        self.nouns['ru'] = nounres[0][0]
        logging.info('Russian: done.')

        nounres = self.cons['fi']['db'].FetchQuery("SELECT count(*) FROM fi_conll WHERE pos IN ('NOUN','P')".format('fi_conll'))
        self.nouns['fi'] = nounres[0][0]
        logging.info('Finnish: done.')

        logging.info("Nouns counted. In Finnish: {}, in Russian: {}".format(self.nouns['fi'],self.nouns['ru']))

    def RawQuery(self, lang, cond, sqlvals, resname):
        logging.info('Querying "{}"'.format(resname))
        cond = "SELECT count(*) FROM {} WHERE ".format(self.cons[lang]['table']) + cond
        res = self.cons[lang]['db'].FetchQuery(cond,sqlvals)
        logging.info('Done.')
        self.results[resname] = res
        return res

class SA_SearchController(SearchController):
    """Control what's being done"""

    def __init__(self, test=False, ext_data=None):
        """Start loggers, get connections etc"""
        StartLogger()
        self.cons = dict()
        self.externaldata = dict()

        if test:
            #For testing, use only the smaller database
            self.cons['fi'] = {'araneum_fi' : psycopg('araneum_fi','juho')}
        else:
            self.cons['fi'] = {'araneum_fi'  : psycopg('araneum_fi','juho'),
                               'press_fi': None}
            self.cons['ru'] = {'araneum_ru'  : psycopg('araneum_ru','juho'),
                               'press_ru': psycopg('press_ru','juho')}
                               #'press_ru': None}

        self.externaldata['press_fi'] = None

        self.metadata = dict()
        logging.info('Fetching metadata...')
        if not test:
            for lang in ['fi','ru']:
                for con_name, con in self.cons[lang].items():
                    logging.info('{},{}'.format(lang, con_name))
                    if con:
                        self.metadata[con_name] = con.FetchQuery('SELECT id, title FROM text_ids',usedict=True)

        logging.info("Connections established.")

        self.results = dict()
        self.searches = dict()


    def Search(self, thisgroup):
        """Hae jokaisesta korpuksesta thisgroup-muuttujalla määritellyn ryhmän lauseita"""

        for con_name, con in self.cons[thisgroup.lang].items():
            logging.info(con_name)

            nogroup = False
            if not con:
                thisgroup.currentsearch.non_db_data = thisgroup.ext_data[con_name]
            else:
                thisgroup.currentsearch.con = con

            thisgroup.currentsearch.Run(nogroup)
            thisgroup.currentsearch.non_db_data = None
            thisgroup.SaveCurrentSearch(con_name)

            SimplifyResultSet(thisgroup.currentsearch) 
            thisgroup.currentsearch.Reset()

def ReadLemmaTuple(fname):
    """Read a list of lemmas from a file and return them as a tuple"""
    with open(fname,"r") as f:
        lemmas = f.read().strip().splitlines()
    return tuple(lemmas)


def ReadLargeJson(fname):
    """RIvi riviltä -yritys"""
    sentence = list()
    sentences = list()
    validsentence = True
    unvalid = 0
    with open(fname,"r") as f:
        for idx, line in enumerate(f):
            if line in ('[\n'):
                pass
            else:
                if line == '{\n':
                    if sentence:
                        if validsentence:
                            sentences.append(sentence)
                        validsentence = True
                    sentence = [line]
                elif "tokenid" in line and validsentence:
                    token_no_pat = re.search('\d+',line)
                    no = token_no_pat.group()
                    if int(no) > 500:
                        unvalid += 1
                        validsentence = False
                    sentence.append(line)
                else:
                    sentence.append(line)
            if idx % 1000000 == 1:
                print('Processed 1 000 000 lines...')

    if validsentence:
        sentences.append(sentence)

    print('{} too long sentences found in {}!'.format(unvalid, fname))

    data = list()
    print('Putting the sentences to data...')
    for idx, sentence in enumerate(sentences):
        sentstring = ''.join(sentence)
        sentstring = sentstring[:-2]
        data.append(json.loads(sentstring))
        if idx % 100 == 1:
            print('Processed {}/{}'.format(idx, len(sentences)),end='\r')
    print('Done.')

    return data

def ReadJson(fname,ask=False):
    if os.path.exists(fname):
        if (ask and input('Käytetäänkö tallennettua objektia? (y/n)') == 'y') or not ask:
            try:
                with open(fname,'r') as f:
                    return json.loads(f.read())
            except MemoryError:
                print('The JSON file is too large, reading in slices...')
                return ReadLargeJson(fname)

    return False

def WriteJson(data,fname):
    with open(fname, 'w') as outfile:
        json.dump(data, outfile,ensure_ascii=False)

def SimplifyResultSet(thisSearch):
    thisSearch.results = list()
    for sentence_id, matches in thisSearch.matches.items():
        for match in matches:
            thisSearch.results.append(match)

def SortResultsByHead(search):
    """ calculate the individual results for each head of the match """
    results = dict()
    for match in search.results:
        if match.CatchHead():
            try:
                results[match.headword.lemma] += 1
            except KeyError:
                results[match.headword.lemma] = 0

    return results 
class CorpusDict(dict):

    def __init__(self, lang, valuelist=False):
        if not valuelist:
            initdict = {'araneum_' + lang :list(),'press_' + lang : list()}
        else:
            initdict = {'araneum_' + lang :valuelist[0],'press_' + lang : valuelist[1]}
        super().__init__(initdict)

def ChooseByQuota(corpusdict, totalcount, analyzeddata):
    totalquota = 0
    amounts = dict()
    for corpus, sentences in corpusdict.items():
        acceptedsentences = list()
        for sentence in sentences:
            #Poista massasta lauseet, jotka on jo analysoitu
            reject = False
            for asentence in analyzeddata:
                if asentence['sent'] == sentence['sent']:
                    reject = True
            if not reject:
                acceptedsentences.append(sentence)
        totalquota += len(acceptedsentences)
        amounts[corpus] = {'quota':len(acceptedsentences),'pick':0}

    if totalquota < totalcount:
        #Jos kaikissa korpuksissa ei yhteensäkään ole tarpeeksi lauseita
        totalcount = totalquota

    reached = 0
    while reached < totalcount:
        #Poimi mahdollisimman tasaisesti kaikista korpuksista, kunnes haluttu kokonaismäärä täynnä
        for corpus in corpusdict.keys():
            if amounts[corpus]['quota'] > 0 and reached < totalcount:
                amounts[corpus]['quota'] -= 1
                amounts[corpus]['pick'] += 1
                reached += 1
    return amounts

def PickAndEvaluate(corpusdict, amounts, analyzeddata):
    remainingcorpusdict = dict()
    picked = list()
    for corpus, sentences in corpusdict.items():
        forbidden = list()
        available_sentences = sentences
        pickedfromthis = list()
        while len(available_sentences) > 0 and len(pickedfromthis) < amounts[corpus]['pick']:
            candidate = random.sample(available_sentences, 1)
            #hae osoite listasta
            for idx, sent in enumerate(available_sentences):
                if sent['sent'] == candidate[0]['sent']:
                    break
            print('{}:{}/{}(tästä kerätty {})'.format(corpus,amounts[corpus]['pick'],len(available_sentences),len(pickedfromthis)))
            accepted = EvalueateSentence(available_sentences, candidate[0], analyzeddata)
            available_sentences.pop(idx)
            if accepted:
                pickedfromthis.append(candidate[0])

        remainingcorpusdict[corpus] = available_sentences
        picked += pickedfromthis
    return {'picked':picked, 'remain':remainingcorpusdict}

def PickForAnalysis(corpusdict,totalcount=15,analyzeddata=list()):
    """ Find x random sentences for further analysis from each corpus"""
    totalquota = 0

    amounts = ChooseByQuota(corpusdict, totalcount, analyzeddata)
    picked = list()
    remainingcorpusdict = dict()

    randomized = PickAndEvaluate(corpusdict, amounts, analyzeddata)

    if len(randomized['picked'])<totalcount:
        #täydennys, jos hylättiin, eikä riittänyt korvaajia
        amounts = ChooseByQuota(randomized['remain'], totalcount-len(randomized['picked']), analyzeddata)
        randomized2 = PickAndEvaluate(corpusdict, amounts, analyzeddata)
        return randomized['picked'] + randomized2['picked']
    else:
        return randomized['picked']

def EvalueateSentence(sentences, sentence, analyzeddata):

    for asentence in analyzeddata:
        #Katso, onko jo valmiiksi analysoitu
        if asentence['sent'] == sentence['sent']:
            print('(Poistettiin vanhastaan analysoitu)')
            return False

    if input('Käykö tämä virke (k/e):\n' + textwrap.fill(sentence['sent']) + '\n\n') == 'e':
        return False
    else:
        return True

def RearrengeSet1Dict(sdict):
    results = list()
    for pod, time in sdict.items():
        for hourname, freq in time.items():
            for i in range(1,int(freq)+1):
                try:
                    results.append({'pod':pod,'hour':int(hourname)})
                except ValueError:
                    results.append({'pod':pod,'hour':hourname})
    return results

def AppendSet1Dict(results, set1combninations, lemmas):
    for match in results:
        numeral = match.matchedword
        if match.matchedword.token in ('часа','часов','часам'):
            #Koska час-sanan kohdalla haku tehdään eri tavalla, numero pitää erikseen kaivaa:
            if hasattr(match.matchedword,"dependentlist"):
                for dep in match.matchedword.dependentlist:
                    if dep.pos == 'M':
                        numeral = dep
        collocates = GetCollocates(match)
        for collocate in collocates:
            if collocate in lemmas:
                try:
                    set1combninations[collocate]
                except KeyError:
                    set1combninations[collocate] = dict()

                try:
                    set1combninations[collocate][WordsToNumbers(numeral.lemma)]
                except KeyError:
                    set1combninations[collocate][WordsToNumbers(numeral.lemma)] = 0

                set1combninations[collocate][WordsToNumbers(numeral.lemma)] += 1

def WordsToNumbers(wordornum):
    try:
        if "до" in wordornum:
            dopat = re.compile('до ?')
            wordornum = dopat.sub('',wordornum)
        if wordornum == "kahden-kolmen":
            #pitäisä päättää...
            return 3
        if ":" in wordornum:
            return int(wordornum[0:wordornum.find(":")])
        if "." in wordornum:
            return int(wordornum[0:wordornum.find(".")])
        if "-ти" in wordornum:
            return int(wordornum[0:wordornum.find("-")])
        if "-х" in wordornum:
            return int(wordornum[0:wordornum.find("-х")])
        if "х" in wordornum:
            return int(wordornum[0:wordornum.find("х")])
        if "lta" in wordornum:
            return int(wordornum[0:wordornum.find("lta")])
        if "klo" in wordornum:
            return int(wordornum.replace("klo",""))
    except ValueError:
        return (wordornum)

    switcher = {
        "час": 1,
        "два": 2,
        "три": 3,
        "четыре":4,
        "пять":5,
        "шесть":6,
        "семь":7,
        "восемь":8,
        "девять":9,
        "десять":10,
        "одиннадцать":11,
        "двенадцать":12,
        "тринадцать":13,
        "четырнадцать":14,
        "пятнадцать":15,
        "шестнадцать":16,
        "семнадцать":17,
        "восемнадцать":18,
        "девятнадцать":19,
        "yksi": 1,
        "kaksi": 2,
        "kolme": 3,
        "neljä":4,
        "viisi":5,
        "kuusi":6,
        "seitsemän":7,
        "kahdeksan":8,
        "yhdeksän":9,
        "kymmenen":10,
        "yksi#toista":11,
        "kaksi#toista":12,
        "kolme#toista":13,
        "neljä#toista":14,
        "viisi#toista":15,
        "kuusi#toista":16,
        "seitsemän#toista":17,
        "kahdeksan#toista":18,
        "yhdeksän#toista":19,
    }

    if wordornum in switcher:
        return switcher[wordornum]
    else:
        try:
            return int(wordornum)
        except ValueError:
            return wordornum


    return switcher.get(wordornum, wordornum)

def GetCollocates(match):
    try:
        n = match.matchedsentence.words[match.matchedword.tokenid+1].lemma
    except KeyError:
        n = None
    try:
        p = match.matchedsentence.words[match.matchedword.tokenid-1].lemma
    except KeyError:
        p = None
    return [p,n]

def IsHeadPreposition(results, preps):
    """Varmista, että pääsanana prepositio"""
    filtered = list()
    for match in results:
        if match.CatchHead():
            if match.headword.token in preps:
                filtered.append(match)
    return filtered

def Ru4bFilter(results, lemmas, prephead, preps=None):
    """Very specific..."""
    filtered = list()
    instr = re.compile('N..si.')
    geninstr = re.compile('N..sg.')

    for match in results:
        added = False
        leftword = match.matchedword
        rightword = match.matchedword
        if prephead:
            #jos prepositioilmaus 
            if match.CatchHead():
                leftword = match.headword
                if (preps and match.headword.token in preps) or not preps:
                    #1. Onko juuri ennen prepositiota (tai ..) sana утро tms. instrumentaalissa
                    #HUOM! Jos välissä on pilkku, ei hyväksytä
                    try:
                        pword = match.matchedsentence.words[leftword.tokenid-1]
                        if pword.lemma in lemmas and instr.match(pword.feat):
                            if pword.lemma != 'день' or pword.token in ('дня','днём'):
                                filtered.append(match)
                                added = True
                    except KeyError:
                        pass

                    #2. onko juuri numeron tai час-sanan jälkeen утро tms. genetiivissä tai instrumentaalissa 
                    if not added:
                        if (preps and match.headword.token in preps) or not preps:
                            try:
                                nword = match.matchedsentence.words[rightword.tokenid+1]
                                if nword.lemma in lemmas and geninstr.match(nword.feat):
                                    if nword.lemma != 'день' or nword.token in ('дня','днём'):
                                        filtered.append(match)
                            except KeyError:
                                pass

    return filtered

def Fi4bFilter(results, lemmas, matchishead, preps=None, kello=False):
    """Very specific..."""
    filtered = list()
    cases = re.compile('Case=(Ade|Ela)')
    adpostype = "post"

    for match in results:
        added = False

        if kello:
            #HACKY!
            leftword = match.matchedsentence.words[int(match.matchedword.tokenid)-1]
        else:
            leftword = match.matchedword

        rightword = match.matchedword

        #1. Määrittele lausekkeen vasen ja oikea laita

        if  preps:
            #Jos lausekkeessa mukana adpositio, hae laidat, muutoin lauseke koostuu vain yhdestä sanasta

            if matchishead:
                #jos parseri analysoinut numeron pääsanaksi
                leftword = None
                for word in match.matchedword.dependentlist:
                    #etsi dependenteistä adpositio ja tarkista, onko se "ennen"
                    if word.token in preps:
                        if word.token in ["ennen"]:
                            #Jos dependenttiadpositio on PREpositio
                            leftword = word
                        else:
                            #Jos dependenttiadpositio on POSTpositio
                            rightword = word
                            leftword = match.matchedword
                        break
            elif match.CatchHead():
                #jos parseri analysoinut adposition pääsanaksi ja pääsana löytyy
                rightword = match.headword

        if leftword:
            try:
                pword = match.matchedsentence.words[leftword.tokenid-1]
            except KeyError:
                pword = None
            try:
                nword = match.matchedsentence.words[rightword.tokenid+1]
            except KeyError:
                nword = None

        #2. Tarkista, onko lausekkeen vasemmalla tai oikealla puolella jokin sanoista "aamulla", "iltapäivästä"  jne..

            if pword:
                if pword.lemma in lemmas and cases.match(pword.feat):
                    filtered.append(match)
                    added = True
            if nword and not added:
                if nword.lemma in lemmas and cases.match(nword.feat):
                    filtered.append(match)

    return filtered

def AnalyzeHeads(results, name):
    heads = list()
    #Listaa pääverbit 
    for match in results:
        match.matchedword.IterateToFiniteHead(match.matchedsentence)
        if match.matchedword.finitehead:
            match.BuildSentencePrintString() 
            heads.append({'ilmaus':name, 'lause':match.matchedsentence.printstring,'pääverbi':match.matchedword.finitehead.lemma,'hakusana':match.matchedword.lemma})
    return heads

def ReportOccurences(results,name,semfunct,lang,lemmacount=0):
    """Kirjoita json R:ää varten. """
    report = list()
    logging.info("Reporting...")
    for match in results:
        match.BuildSentencePrintString() 
        match.matchedword.IterateToFiniteHead(match.matchedsentence)
        headverb = 'None'
        if match.matchedword.finitehead:
            headverb = match.matchedword.finitehead.lemma
        report.append({'ilmaus':name, 'lemma':match.matchedword.lemma, 'virke':match.matchedsentence.printstring,'semfunct':semfunct, 'pääverbi': headverb, 'lemmafreq': lemmacount, 'lang':lang})
    return report


def CollectVerbLemmas(results):
    datarows = list()
#    for result in results:
#        result.
#        datarows.append({'sentence':m.PrintSentence,'lemma':m.matchedword.lemma, 'contextlemmas':'')})


### ANALYSES:

#1. Transitive clauses

def AnalyzeTransitive(data, searches, lang, p2active=False):
    if p2active:
        foranalysis = {'beforeverb_and_subject':CorpusDict(lang), 'beforeverb':CorpusDict(lang),'beforeobject':CorpusDict(lang),'afterobject':CorpusDict(lang),'failed':CorpusDict(lang)}
    else:
        foranalysis = {'beforeverb':CorpusDict(lang),'beforeobject':CorpusDict(lang),'afterobject':CorpusDict(lang),'failed':CorpusDict(lang)}

    for corpusname, search in searches.items():

        for result in search:
            result.BuildSentencePrintString() 
            try:
                text_id = int(result.matchedword.sourcetextid)
                metarow = GetMetadata(text_id,data.metadata[corpusname])
                sourcetext = metarow['title']
            except ValueError:
                sourcetext = result.matchedword.sourcetextid

            try:
                analysisrow =  {'tokenid':result.matchedword.tokenid, 'sentid':result.matchedsentence.sentence_id,'sent':result.matchedsentence.printstring,'dfunct':'','analyzed':False, 'source':corpusname, 'headverb':result.matchedword.finitehead.lemma,'headverbdep':result.matchedword.finitehead.deprel,'sourcetext':sourcetext}
                #import ipdb; ipdb.set_trace()
                foranalysis[result.TransitiveSentenceDistancies(p2active)][corpusname].append(analysisrow)
            except AttributeError:
                logging.info('No finite head for sent {}!'.format(result.matchedsentence.printstring))

    return foranalysis

def AnalyzeInformationStructure(dictrow):
    """Questions to help in analyzing the IS of a sentence"""

    print('\n' + textwrap.fill(dictrow['sent']) + '\n')


    tf = multimenu({'t':'topiikki','f':'fokus','d':'Poista tämä analysoitavista'},'Ennemmin topiikki vai fokus?')

    if tf.answer == 'd':
        return False
    elif tf.answer == 't':
        dfanswers = {'a':'a-topiikki','s':'s-topiikki','as':'additiivinen s-topiikki','vs':'varsinainen s-topiikki','ki':'implisiittinen k-topiikki','ke':'eksplisittinen k-topiikki'}
    else:
        dfanswers = {'s':'semanttinen fokus','kk':'Korjaava kontrastinen fokus','tk':'Toteava kontrastinen fokus'}

    dftype = multimenu(dfanswers,'Valitse alalaji')

    # Erikseen vielä kysymys subjektista:
    subf = multimenu({'a':'aktivoitu','sa':'semiaktiivinen','n':'aktivoimaton'},'Millainen D-status subjektilla?')


    dictrow['dfunct'] = tf.answer + "_" + dftype.answer
    dictrow['subfunct'] = subf.answer

    return dictrow



