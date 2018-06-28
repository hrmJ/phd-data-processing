import sys
import os
import glob
import json
import time
from sys import platform as _platform
import searchutils
import menus
result_data_address = '/tmp/results'
final_data_address = '/tmp'
pickedamount = 20


#========================================

def Quit():
    pass

def ListAnalyzedGroups():
    langs = menus.multimenu({'fi':'suomi','ru':'venäjä'},'Valitse kieli')
    groups = {}
    groups_display = {}
    for idx, filename in enumerate(glob.glob('{d}/{l}/*.json'.format(d=result_data_address, l=langs.answer))):
        lastslash = filename.rfind('/')
        ending = filename.rfind('.')
        groupname = filename[lastslash+1:ending]
        groups[str(idx)] = groupname

        targetdatafile = '{a}/{l}/{g}.json'.format(l=langs.answer, g=groupname, a=final_data_address)
        if os.path.isfile(targetdatafile):
            groups_display[str(idx)] = groupname + " [x]"
        else:
            groups_display[str(idx)] = groupname + " [_]"

        groups[str(idx)] = groupname
    if groups:
        groupmenu = menus.multimenu(groups_display,'Valitse analysoitava ryhmä',sortanswers=True)
        AnalyzeGroup(groups[groupmenu.answer], langs.answer)
    else:
        print('Sori. Ei dataa.')

def GetPositionNames(posname):
    if 'svo' in posname:
        return ["beforeverb_and_subject", "beforeverb", "beforeobject", "afterobject"]
    else:
        return ["beforeverb", "afterverb"]

def GetSentencesByPos(data, posname, language, targetdata):
    """
    Funktio luotu 1.9.2016.
    Tarkoitus ladata ja järjestellä filtteröity data informaatiorakenteen analyysia varten
    korpuksen ja lauseaseman mukaisiin ryhmiin.
    """
    sentences = searchutils.CorpusDict(language)
    already_analyzed_sentences = list()

    for sentence in targetdata:
        if sentence['location'] == posname:
            already_analyzed_sentences.append(sentence)

    for sentence in data:
        if sentence['location'] == posname:
            for corpusname in sentences.keys():
                if sentence['corpus'] == corpusname:
                    sentences[corpusname].append(sentence)

    return {'rawdata':sentences,'analyzeddata':already_analyzed_sentences}

def CollectData(quant=False):
    """
    Funktio luotu 1.9.2016.
    Tämän funktion tarkoituksena puhtaasti kerätä data tietokannasta ja
    tallentaa se valmiiksi syntaktisiksi ja semanttisiksi ryhmiksi kuten
    lc0a_svo.
    """
    import utils

    langs = menus.multimenu({'fi':'suomi','ru':'venäjä'},'Valitse kieli')
    if langs.answer == 'fi':
        from groups.fi import subgroups
    elif langs.answer == 'ru':
        from groups.ru import subgroups

    groupnamelist = {}
    grouplist = {}
    idx = 1
    for subgroupname, subgroup in subgroups.items():
        groupnamelist[str(idx)] = subgroupname
        grouplist[str(idx)] = subgroup
        idx += 1

    groupmenu = menus.multimenu(groupnamelist,'Mikä ryhmä kerätään?',sortanswers=False)
    #grouplist = groupmenu.validanswers

    grouplist[groupmenu.answer].Analyze(quant)

def CollectQuantData():
    CollectData(True)

def Quant():
    """Testaukseen käytettävä funktio. Yritetään miettiä, saisiko järkevää kvant.analyysia tällä datalla. Toisin
    sanoen parantaa precisionia filttereissä. Funktio luotu 22.9.2016"""
    import utils
    from groups.fi import subgroups
    sg = subgroups['lc0a']
    sg.Load('press_fi')
    filt = utils.filters.Filter(sg.corpora['press_fi'],'fi')
    filt.ByOrder('SOV', False)
    filt.DirectLinkToVerb()
    filt.Ohjelmatiedot()
    input('...')
    for match in filt.passed:
        match.matchedsentence.BuildDependencyString()
        match.matchedsentence.buildPrintString()
        pos = match.TransitiveSentenceDistancies(True,'fi',match.matchedsentence, True)
        print(match.matchedsentence.sentence_id)
        input("{}:\n\n {}\n\n{}".format(pos, match.matchedsentence.printstring, match.matchedsentence.depstring))

    #Tutki dependenssikuvaimia:
    #
    #for match in filt.passed:
    #    match.matchedsentence.BuildDependencyString()
    #    match.matchedsentence.buildPrintString()
    #    input("{}\n\n{}".format(match.matchedsentence.printstring, match.matchedsentence.depstring))

def PerformIsAnalysis(rawdata, location, targetdatafile, targetdata, analyzeddata):
    """
    rawdata = corpusdict
    location = 'beforeverb jne'
    """

    #Vähennä tavoitteesta ensin vanhastaan analysoitujen määrä
    pickthistime = pickedamount - len(analyzeddata)

    sentences = searchutils.PickForAnalysis(rawdata, pickthistime, analyzeddata)
    count = 0
    for sentence in sentences:
        count += 1
        sentence.update({'location':location,'time_of_analysis':time.strftime('%c')})
        searchutils.logging.info('\n Analyzing {} of {} sentences, source: {} \n'.format(count,len(sentences),sentence['sourcetext']))
        analyzed = searchutils.AnalyzeInformationStructure(sentence)
        if analyzed:
            #Jos lause analysoitiin eikä hylätty
            targetdata.append(analyzed)
            #Tallenna jokaisen lauseen jälkeen
            searchutils.WriteJson(targetdata, targetdatafile)
    input('Valmis. Paina enter jatkaaksesi')

def AnalyzeGroup(groupname, language):
    """
    funktio luotu 1.9.2016. tarkoituksena oisi, että tälle funktiolle syötetään
    result_data_address-muuttujaan tallennetun sijainnin kautta löytyviä
    varsinaisia sanaryhmiä kielikohtaisesti, esim. fi:lc0a_svo, ru:lc0a_svo ym.
    """

    posnames = GetPositionNames(groupname)
    input('Aloitetaan siis analysoimaan kielen {} ryhmää {}.\n Analysoidaan seuraavat positiot: {}\n{}\n\n'.format(language, groupname, ', '.join(posnames),'='*40))

    sourcedata = searchutils.ReadJson('{d}/{l}/{g}.json'.format(d=result_data_address, l=language, g=groupname))
    targetdatafile = '{a}/{l}/{g}.json'.format(l=language, g=groupname, a=final_data_address)
    targetdata = list()

    if os.path.isfile(targetdatafile):
        targetdata = searchutils.ReadJson(targetdatafile)

    for position in posnames:
        #Hae kaikki lauseet, joissa ajanilmaus ko sijainnissa (ennen verbiä, ennen objektia yms.)
        all_sentences = GetSentencesByPos(sourcedata, position, language, targetdata)
        input('POIMITAAN asemaan {} (paina enter)'.format(position))
        PerformIsAnalysis(all_sentences['rawdata'], position, targetdatafile, targetdata, all_sentences['analyzeddata'])


# ========================================

if __name__ == "__main__":

    if sys.argv[1] == "allfi":
        #Jos tarkoitus analysoida kaikki, mitä on. VIE KAUAN!
        import utils
        import groups.fi
        #import groups.ru
        quant=True
        searchutils.StartLogger('/tmp/groups.log')
        counter = 0
        for subgroupname, subgroup in groups.fi.subgroups.items():
            counter += 1
            res_filename = '{}/fi/{}_SVO_quantdata.json'.format(result_data_address, subgroupname)
            if not os.path.isfile(res_filename):
                searchutils.logging.info("STARTING "  + subgroup.name + " ({} / {})".format(counter, len(groups.fi.subgroups)))
                subgroup.Analyze(quant)
                searchutils.logging.info(subgroup.name + "DONE.")
            else:
                searchutils.logging.info(subgroup.name + "already analyzed, skipping...")

    elif sys.argv[1] == "allru":
        #Jos tarkoitus analysoida kaikki, mitä on. VIE KAUAN!
        import utils
        import groups.ru
        quant=True
        searchutils.StartLogger('/tmp/groups_ru.log')
        counter = 0
        for subgroupname, subgroup in groups.ru.subgroups.items():
        #for subgroupname, subgroup in groups.ru.testgroups.items():
            counter += 1
            res_filename = '{}/ru/{}_SVO_quantdata.json'.format(result_data_address, subgroupname)
            if not os.path.isfile(res_filename):
                searchutils.logging.info("STARTING "  + subgroup.name + " ({} / {})".format(counter, len(groups.ru.subgroups)))
                subgroup.Analyze(quant)
                searchutils.logging.info(subgroup.name + "DONE.")
            else:
                searchutils.logging.info(subgroup.name + "already analyzed, skipping...")
    elif sys.argv[1] == "test":
        print("Entering test mode....")
        import utils
        from groups.fi import subgroups
        #from groups.ru import subgroups
        subgroups['lc0a'].Analyze(True,True)
        sys.exit(0)
    elif len(sys.argv)>1:
        import utils
        if sys.argv[1] == "fi":
            import groups.fi as agroups
        if sys.argv[1] == "ru":
            import groups.ru as agroups
        subgroupname = sys.argv[2]
        subgroup =  agroups.subgroups[subgroupname]
        searchutils.StartLogger('/tmp/groups.log')
        res_filename = '{}/fi/{}_svo_quantdata.json'.format(result_data_address, subgroupname)
        searchutils.logging.info("STARTING "  + subgroup.name)
        subgroup.Analyze(True)
        searchutils.logging.info(subgroup.name + "DONE.")

#    except IndexError:
#        #Jos ajat ohjelmana ja valitset itse, mikä ryhmä analysoidaan
#        mainmenu = menus.multimenu({'q':'lopeta','a':'analysoi yksittäisiä ryhmiä','k':'kerää dataa','kva':'Tallenna dataa kvantitatiivista analyysia varten'})
#        actions  = {'a':ListAnalyzedGroups,'q':Quit,'k':CollectData,'kva':CollectQuantData}
#        mainmenu.answer = ""
#        while mainmenu.answer != 'q':
#            actions[mainmenu.prompt_valid('Tervetuloa! Mitä tehdään?')]()

        ##Jos pitää testata pelkkää hakua:
        #import utils
        #from groups.fi import subgroups
        #g = subgroups['ex3a']
        #g.currentsearch.con = g.cons['press_fi']
        #g.currentsearch.Run(False)
    
