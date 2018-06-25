from datascripts import searchutils, glob
import filters
import sys
import os
import re
import gc
import time
from datascripts import result_data_address

rawkorpaddress = '/tmp'
saved_data_address = '/tmp'

def LoadKorpData(fnames, outputtext=False):
    korpdata = list()
    if outputtext:
        outputsentences = list()
        outputsources = list()

    for fname in glob.glob(fnames):
        if outputtext:
            outputdict = searchutils.ParseKorpJson(searchutils.ReadJson(fname), outputtext)
            outputsentences.append('\n!!!!\n'.join(outputdict['sentences']))
            outputsources.append('\n'.join(outputdict['sources']))
        else:
            korpdata += searchutils.ParseKorpJson(searchutils.ReadJson(fname), outputtext)

    if outputtext:
        foldpat = re.search('/([^/]+)/[^/]+$',fnames)
        groupname = foldpat.groups(0)
        try:
            with open('/cygdrive/c/data/korp_to_parse/{}.txt'.format(groupname[0]),'w') as f:
                f.write('\n!!!!\n'.join(outputsentences))
            with open('/cygdrive/c/data/korp_to_parse/{}.sources.txt'.format(groupname[0]),'w') as f:
                f.write('\n'.join(outputsources))
        except FileNotFoundError:
            with open('data/korpdata/{}.txt'.format(groupname[0]),'w') as f:
                f.write('\n!!!!\n'.join(outputsentences))
            with open('data/korpdata/{}.sources.txt'.format(groupname[0]),'w') as f:
                f.write('\n'.join(outputsources))
        print('Wrote {}'.format(groupname[0]))

    return korpdata


class Group():
    currentgroup = None
    def __init__(self,name,lang,condcol,prevcond=None,nextcond=None,depcond=None,secondpreviouscond=None,secondnextcond=None,countcomma=True,thirdnextcond=None, name_in_db=None, lengthmeter=[0,0]):
        self.name = name
        self.lang = lang
        self.ext_data = dict()
        self.corpora = searchutils.CorpusDict(self.lang)
        self.Initsearch(name_in_db)
        self.cons = cons.connections[lang]
        self.results = dict()
        self.currentsearch.ConditionColumns = condcol
        self.currentsearch.beforecommacountsaslast = countcomma
        self.lengthmeter = lengthmeter
        #Additional search parameters
        addconds = {'prevcond':prevcond, 'nextcond':nextcond, 'depcond2':depcond,'secondpreviouscond': secondpreviouscond,'secondnextcond': secondnextcond,'thirdnextcond': thirdnextcond}
        for condname, condvals in addconds.items():
            self.SetAdditionalCond(condname, condvals)

    def SetAdditionalCond(self, condname, condvals):
        """Sets some additional search parameters"""
        if condvals:
            #if isinstance(condvals[1], str):
            #    condvals[1] = (condvals[1],)
            setattr(self.currentsearch,condname,{'column':condvals[0],'values':condvals[1]})

    def Initsearch(self, name_in_db):
        self.currentsearch = searchutils.Search(pseudo=True)
        self.currentsearch.isparallel = False
        self.currentsearch.toplevel = "sentence_id"
        self.currentsearch.non_db_data = None
        self.currentsearch.limited = False
        self.currentsearch.queried_table = self.lang + "_conll"
        if not name_in_db:
            self.currentsearch.groupname = self.name
        else:
            self.currentsearch.groupname = name_in_db

        if self.name in ('ex1a1', 'ex1a2', 'ex1a'):
            #Jälkisäätöä, kun teknisistä syistä erotettava 2 ryhmää
            self.currentsearch.groupname = 'ex1'

    def GetKorpData(self):
        print('\tSerializing external data from korp...')
        korpaddress = '{}/{}/*json'.format(rawkorpaddress, self.name)
        self.ext_data['press_fi'] = LoadKorpData(korpaddress)

    def SaveCurrentSearch(self, corpusname):
        print('Serializing the search to {}'.format(saved_data_address))
        directory = '{}/{}/{}/'.format(saved_data_address, self.lang, self.name)
        #Luo kansio tälle ryhmälle, jos ei vielä ole
        if not os.path.exists(directory):
            os.makedirs(directory)
        fname = '{}/{}.json'.format(directory, corpusname)
        try:
            self.currentsearch.SerializeMonoMatches(fname)
        except Exception as e:
            input('Failed to serialize! ' + repr(e) + 'PAINA ctrl-c keskeyttääksesi tai enter jatkaaksesi')
        CleanSerializedData(fname)

    def Load(self, picked=None):
        print('\tLoading serialized data...')
        for corpusname, corpusdata in self.corpora.items():
            do = True
            if picked and corpusname != picked:
                #Mahdollista testaaminen vain yhdellä tietyllä korpuksella
                do = False
            if do:
                rawdata = searchutils.ReadJson('{}/{}/{}/{}.json'.format(saved_data_address, self.lang, self.name, corpusname))
                if rawdata:
                    self.corpora[corpusname] = searchutils.ParseMatchList(rawdata)
                    print('\t \t Succesfully loaded the data for {}'.format(corpusname))
                else:
                    print('\t \t No data saved for {}'.format(corpusname))
                    self.corpora[corpusname] = None

    def GetData(self, istest=False):
        self.Load()
        for corpus, data in self.corpora.items():
            if not data:
                print('No pre-saved data, therefore QUERYING now {} for {}'.format(corpus, self.name))
                con = self.cons[corpus]
                nogroup = False
                self.currentsearch.con = con
                self.currentsearch.Run(nogroup)
                self.currentsearch.non_db_data = None
                self.SaveCurrentSearch(corpus)
                searchutils.SimplifyResultSet(self.currentsearch) 
                #SET the data:
                self.corpora[corpus] = self.currentsearch.results
                self.currentsearch.Reset()

    def GetSentences(self, quant=False):
        print("Filtering out SVO and SOV sentences for {}.{}".format(self.lang, self.name))
        self.results = {}
        for corpus, data in self.corpora.items():
            print(corpus)
            # Quant vaikuttaa muun muassa objektitulkinnan tiukkuuteen -->
            for order in ["SVO", "SOV"]:
                filt = filters.Filter(data, self.lang)
                print("TADAA!!: " + order)
                if order not in self.results:
                    self.results[order] = list()
                filt.ByOrder(order, quant)
                if quant:
                    #Tarkempi filtteri kvantitatiivista analyysia varten
                    filt.DirectLinkToVerb()
                    filt.Ohjelmatiedot()
                print('\t Defining distancies for {} {}...'.format(order, corpus))
                if filt.passed:
                    for result in filt.passed:
                        self.results[order].append(
                                result.PrintInfoDict(
                                    {
                                        'location':result.TransitiveSentenceDistancies(True,self.lang,result.matchedsentence,order=order),
                                        'corpus': corpus, 
                                        'sourcetext':cons.GetMetaRow(result, corpus, self.lang)
                                    }
                                    )
                                )

    def SaveResults(self, quant):
        print('Saving the results to {}'.format(result_data_address))
        for subgname, datalist in self.results.items():
            print('\t {}'.format(subgname))
            if quant:
                searchutils.WriteJson(datalist,'{}/{}/{}_{}_quantdata.json'.format(result_data_address,self.lang,self.name, subgname))
            else:
                searchutils.WriteJson(datalist,'{}/{}/{}_{}.json'.format(result_data_address,self.lang,self.name, subgname))

    def Analyze(self, quant, istest=False):
        """Koko analyysiprosessi kaikkine alaryhmineen, niin että lopuksi tiedot tallennetaan 
        alaryhmittäin json-tiedostoihin"""
        searchutils.Search.lengthmeter = self.lengthmeter
        self.GetData()
        self.GetSentences(quant)
        self.SaveResults(quant)


class Connector():
    """Create connections to all the corpora for both languages"""

    def __init__(self, testlang=None):

        print('Establishing connections to database...')
        self.connections = {'fi':None,'ru':None}
        #self.connections = {'fi':None}
        if testlang:
            self.connections = {testlang:None}
        for lang in self.connections.keys():
            self.connections[lang] = searchutils.CorpusDict(lang,[searchutils.psycopg('araneum_' + lang), searchutils.psycopg('press_' + lang)])
        print("Connections established.")

    def GetMetaRow(self, result, corpus, lang):
        """Hae metadatatiedot sanan id:n perusteella"""
        try:
            text_id = int(result.matchedword.sourcetextid)
            title = self.connections[lang][corpus].FetchQuery('SELECT title FROM text_ids WHERE id = %s',(text_id,))
            sourcetext = title[0][0]
        except ValueError:
            sourcetext = result.matchedword.sourcetextid
        except IndexError:
            sourcetext = "textid {}".format(text_id)
        except KeyError:
            if corpus == 'press_fi':
                print('Korp-lähteen määrittäminen ongelmallista.')
                #import ipdb; ipdb.set_trace()
            sourcetext = "undefined"

        return sourcetext

class ResultDict(dict):

    def __init__(self, lang, valuelist=False):
        if not valuelist:
            initdict = {'araneum_' + lang :list(),'press_' + lang : list()}
        else:
            initdict = {'araneum_' + lang :valuelist[1],'press_' + lang : valuelist[2]}
        super().__init__(initdict)


def CleanSerializedData(fname):
    """Siltä varalta, että liian pitkiä lauseita araneum-hakutuoksissa"""
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


    if unvalid > 0:
        print('{} too long sentences found in {}!'.format(unvalid, fname))
        lines = ""
        print('joining sentences...')
        for idx, sentence in enumerate(sentences):
            lines += ''.join(sentence)
            if idx % 1000 == 1:
                print('Processed {}/{}'.format(idx, len(sentences)),end='\r')

        print('writing...')
        with open(fname, "w") as f:
            f.write("[\n" + lines)


if len(sys.argv)>1 and __name__ == "__main__":
    kd = LoadKorpData("{}/*".format(sys.argv[1]), True)
else:
    if len(sys.argv)>1:
        if (sys.argv[1]=='test'):
            cons = Connector(testlang='fi')
    cons = Connector()
