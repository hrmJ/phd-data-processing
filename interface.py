#! /usr/bin/env python
import codecs
import textwrap
import random
import csv
from deptypetools import makeSearch
import sys
from collections import defaultdict
from lxml import etree
import string
import re
import os
import os.path
#local modules
from dbmodule import mydatabase, psycopg
from menus import Menu, multimenu, yesnomenu 
from search import Search, Match, Sentence, Word, ConstQuery, Db 
from tools.objecttools import savepickle, loadpickle
import datetime
import glob
from texttable import Texttable, get_color_string, bcolors

class MainMenu:
    """This class include all
    the comand line menu options and actions"""
    mainanswers =  {'q':'quit','2':'select language', '3':'Toggle parallel search on/off',
            '1':'select database','5':'View searches','6':'View saved searches',
            '7':'Corpus stats','4':get_color_string(bcolors.RED,'Concordances')}

    def __init__(self):
        self.menu = multimenu(MainMenu.mainanswers)
        # Selectable options:
        self.selectedlang = 'none'
        self.selecteddb = 'none'
        self.isparallel = 'no'
        self.searchcommitted = False
        self.columns = dict()
        #Control the program flow
        self.run = True
        self.pause = False
        self.conditionset = None

    def runmenu(self):
        'Run the main menu'
        #If all necessary prerequisites are set, initialize the possible conditions
        #Clear the terminal:
        os.system('cls' if os.name == 'nt' else 'clear')
        #Build the selected options
        self.menu.question = 'Welcome\n\n' + '='*40 + \
                          '''\n\nSelected options: 
                             \nDatabase: {db}\nLanguage: {lang} \nParallel Concordances: {parc} {wspace}
                             '''.format(db=self.selecteddb,lang=self.selectedlang, parc=self.isparallel, wspace='\n'*2 + '='*40 + '\n'*2)
        self.menu.validanswers = MainMenu.mainanswers
        self.menu.prompt_valid()
        self.MenuChooser(self.menu.answer)
        #Show language if selected:

    def chooselang(self):
        self.menu.question = 'Select language: '
        self.menu.validanswers = {'f':'finnish','r':'russian'}
        self.menu.prompt_valid()
        #Evaluate:
        if self.menu.answer == 'f':
            Db.searched_table = 'fi_conll'
            self.selectedlang = 'fi'
        elif self.menu.answer == 'r':
            Db.searched_table = 'ru_conll'
            self.selectedlang = 'ru'
        if self.selecteddb != 'none':
            print('Initializing configuration...')
            self.conditionset = ConditionSet(self.selecteddb)


    def choosedb(self):
        self.menu.question = 'Select database: '
        self.menu.validanswers = {'1':'syntparfin2','2':'syntparrus2','3':'russian_ext','4':'tbcorpfi','5':'tbcorpfinnish'}
        self.menu.prompt_valid()
        Db.con = mydatabase(self.menu.validanswers[self.menu.answer],'juho')
        self.selecteddb = self.menu.validanswers[self.menu.answer]
        if self.selectedlang != 'none':
            print('Initializing configuration...')
            self.conditionset = ConditionSet(self.selecteddb)

    def testSettings(self):
        if self.selecteddb == 'none':
            return input('Please select a database first!')
        if self.selectedlang == 'none':
            return input('Please select a language first!')
        return True

    def Parconc(self):
        """The actual concordancer"""
        if self.testSettings():
            if self.searchcommitted:
                self.conditionset.ResetConditions()
            self.conditionset.AddConditions()
            parallelon = False
            if self.isparallel == 'yes':
                parallelon = True
           # addheadcond = input('Press enter to move on, h to add conditions concerning the head of the matching word')
           # if addheadcond == 'h':
           #     self.conditionset.AddConditions(headcond=True)
            if parallelon:
                self.search = makeSearch(database=Db.con.dbname, dbtable=Db.searched_table, ConditionColumns=self.conditionset.condcols,headcond=self.conditionset.headcols, isparallel=parallelon)
            else:
                self.search = makeSearch(database=Db.con.dbname, dbtable=Db.searched_table, ConditionColumns=self.conditionset.condcols,headcond=self.conditionset.headcols, isparallel=parallelon, monoling=True)
            printResults(self.search)
            self.searchcommitted = True

    
    def viewsearches(self):
        """Take a look at the conducted searches and repeat / save them"""
        #collect the answers in a dict
        answlist = dict()
        for idx, searchobject in enumerate(Search.all_searches):
            answlist[str(idx)] = searchobject.name
        answlist['c'] = "Cancel"
        try:
            pickedsearch = Search.all_searches[int(self.menu.redifine_and_prompt('Select a search',answlist))]
            self.menu.redifine_and_prompt('What do you want to do with this search?',{'s':'save','r':'re-show the results'})
            if self.menu.answer == 's':
                filename = "savedsearches/{}_{}.p".format(pickedsearch.name,datetime.date.today())
                pickedsearch.filename = filename
                filenumber = 2
                while os.path.exists(filename):
                    filename = "savedsearches/{}_{}{}.p".format(pickedsearch.name,datetime.date.today(),filenumber)
                    pickedsearch.filename = filename
                    filenumber += 1
                pickle.dump(pickedsearch, open(filename, "wb"))
            elif self.menu.answer == 'r':
                printResults(pickedsearch)
        except:
            pass

    def viewsavedsearches(self):
        """Take a look at the saved searches and append them to the lsit of searches"""
        #collect the answers in a dict
        answlist = dict()
        if glob.glob('savedsearches/*.p'):
            for idx, savedsearch in enumerate(glob.glob('savedsearches/*.p')):
                answlist[str(idx)] = savedsearch
            answlist['c'] = "Cancel"
            pickedsearch = answlist[self.menu.redifine_and_prompt('Load a saved search:',answlist)]
            try:
                Search.all_searches.append(loadpickle(pickedsearch))
                print('Search {} loaded succesfully. Press "View searches" in the main menu to view it'.format(pickedsearch))
            except:
                print('No search loaded')
        else:
            print('No saved searches found.')

    def MenuChooser(self,answer):
        os.system('cls' if os.name == 'nt' else 'clear')
        if answer == 'q':
            self.run = False
        elif answer == '2':
            self.chooselang()
        elif answer == '1':
            self.choosedb()
        elif answer == '3':
            if self.isparallel == 'no':
                self.isparallel = 'yes'
            else:
                self.isparallel = 'no'
        elif answer == '5':
            self.viewsearches()
            self.pause = True
        elif answer == '6':
            self.viewsavedsearches()
        elif answer == '4':
            self.pause=True
            self.Parconc()
        elif answer == '7':
            statmen = Statmenu()
            statmen.runmenu()

    def ListColumns(self):
        if not self.columns:
            psycon = psycopg(self.selecteddb,'juho')
            rows = psycon.FetchQuery('SELECT column_name FROM information_schema.columns WHERE table_name = %s',(Db.searched_table,))
            for idx, row in enumerate(rows):
                self.columns[str(idx)] = row[0]

class ConditionSet:
    """...."""
    ignoredcolumns = ['contr_deprel','contr_head','id','sentence_id','align_id','text_id','translation_id','head']

    def __init__(self, selecteddb):
        self.columnnames = dict()
        self.columns = dict()

        #Initialize printed options
        self.optionstring = ''
        self.optiontable = Texttable()
        self.optiontable.set_cols_align(["l", "l"])
        self.optiontable.set_cols_valign(["m", "m"])
        self.optiontable.add_row(['Column','Possible values'])
        self.FormatOptionString()
        self.condcols = None
        self.headcols = None

        psycon = psycopg(selecteddb,'juho')
        rows = psycon.FetchQuery('SELECT column_name FROM information_schema.columns WHERE table_name = %s',(Db.searched_table,))
        colindex = 1
        for row in rows:
            #Add a new column object to the columnlist if it makes sense to add it
            if row[0] not in ConditionSet.ignoredcolumns:
                self.columns[colindex] = ConllColumn(name = row[0],con = psycon)
                self.columnnames[str(colindex)] = self.columns[colindex].screenname
                colindex += 1

    def ResetConditions(self):
        self.optionstring = ''
        self.optiontable = Texttable()
        self.optiontable.set_cols_align(["l", "l"])
        self.optiontable.set_cols_valign(["m", "m"])
        self.optiontable.add_row(['Column','Possible values'])
        self.FormatOptionString()
        self.condcols = None
        self.headcols = None
        for key, column in self.columns.items():
            column.presetvalues = dict()
            column.regexcond = False
            column.negativeconds = False
            #just initianiling a variable for the picksearchedval method
            column.addmorevalues = True


    def AddConditions(self, headcond=False):
        """Parallel concordance search"""
        conditiondict = dict()
        columnmenu = multimenu(self.columnnames)
        addmoreconditions = multimenu({'y':'add more','q':'stop adding conditions'})
        addmoreconditions.answer = 'y'
        while addmoreconditions.answer == 'y':
            vals = list()
            columnmenu.prompt_valid(self.optionstring + 'What column should the condition be based on?')
            thiscolumn = self.columns[int(columnmenu.answer)]
            while thiscolumn.addmorevalues:
                vals.append(thiscolumn.PickSearchValue())
            if thiscolumn.regexcond:
                conditiondict["#" + thiscolumn.name] = vals[-1]
                self.FormatOptionString([thiscolumn.screenname, 'REGEX: ' + vals[-1]])
            elif thiscolumn.negativeconds:
                conditiondict["!" + thiscolumn.name] = tuple(vals)
                self.FormatOptionString([thiscolumn.screenname, 'NOT EQUAL TO: ' + ' OR '.join(vals)])
            else:
                conditiondict[thiscolumn.name] = tuple(vals)
                self.FormatOptionString([thiscolumn.screenname, ' OR '.join(vals)])
            addmoreconditions.prompt_valid(self.optionstring + 'Keep adding search conditions?')
        if headcond:
            self.headcols = conditiondict
        else:
            self.condcols = conditiondict

    def FormatOptionString(self,row=None):
        header = 'Current search conditions:\n{}\n\n'.format('='*30)
        if row:
            self.optiontable.add_row(row)
        self.optionstring = header + self.optiontable.draw() + "\n\n\n"


class ConllColumn:
    """For every searchable column there is an object that includes possible values etc."""
    presetvalues = ['pos','deprel']
    descriptivenames = {'feat':'Grammatical features','pos':'Part of speech','deprel':'Dependency role','tokenid':'The ordinal position of token in the sentence'}
    def __init__(self, name, con):
        self.name = name
        self.presetvalues = dict()
        self.regexcond = False
        self.negativeconds = False
        #just initianiling a variable for the picksearchedval method
        self.addmorevalues = True
        #if possible, use a more user-friendly name to be shown
        try:
            self.screenname = ConllColumn.descriptivenames[name]
        except KeyError:
            self.screenname = name[0].upper() + name[1:]

        #If the values should not be freely determined but rather chosen from an existing list
        if name in ConllColumn.presetvalues:
            rows = con.FetchQuery('SELECT {colname}, count({colname}) FROM {table} group by 1 order by 2 DESC'.format(colname = self.name, table = Db.searched_table))
            for idx, row in enumerate(rows):
                self.presetvalues[str(idx)] = row[0]

        #Add a menu for asking for more values
        self.askmoremenu = multimenu({'y':'yes','n':'no'})
        self.askmoremenu.question = 'Keep adding possible search values for this column?'

    def PickSearchValue(self):
        """Select a value to be used in a search"""
        if not self.presetvalues:
            os.system('cls' if os.name == 'nt' else 'clear')
            headerstrings = ["Give a value the column {} should have.".format(get_color_string(bcolors.BLUE,self.screenname)),
                      "- If you want to use a regex, surround the string with forward slashes (e.g. /^[m|M]yregexstri.*/)",
                      "- If this  is  a negative condition, begin the first condition with a ! (e.g. !dontmatchthis)",
                      "- Press l to load a list of values from an external file\n>"]
            value = input('\n'.join(headerstrings))
            if value == 'l':
                self.addmorevalues = False
                return LoadCsv()
            elif value[0] == '/' and value[-1] == '/':
                self.addmorevalues = False
                self.regexcond = True
                return value.strip('/')
            elif value[0] == '!' or self.negativeconds:
                self.negativeconds = True
                returnvalue = value[1:]
            else:
                returnvalue =  value
        else:
            valuemenu = multimenu(self.presetvalues,'Pick a value the column {} should have '.format(get_color_string(bcolors.BLUE,self.screenname)))
            returnvalue =  valuemenu.validanswers[valuemenu.answer]

        self.askmoremenu.prompt_valid()
        if self.askmoremenu.answer == 'y':
            self.addmorevalues = True
        else:
            self.addmorevalues = False

        return returnvalue




class Statmenu:
    menuoptions = {'1':'Word count','2':'Word count for monolingual corpora', '3':'Word count for the WHOLE monolingual corpus', 'c':'Return to main menu'}
    def __init__(self):
        self.menu = multimenu(Statmenu.menuoptions)
        self.menu.question = 'Select the function you would like to apply:'

    def wordCountForText(self, text_id, table):
        """Count the number of words in a given text and return it as a string"""
        query = 'SELECT count(*) from {} WHERE token NOT IN %(punct)s AND text_id = %(text_id)s'.format(table)
        res = Db.con.nondictquery(query,{'punct':tuple(string.punctuation),'text_id':text_id})
        return str(res[0][0])

    def wordCountForAll(self, table):
        """Count the number of words in the whole corpus and return it as a string"""
        query = 'SELECT count(*) from {} WHERE token NOT IN %(punct)s'.format(table)
        res = Db.con.nondictquery(query,{'punct':tuple(string.punctuation)})
        print("{} words in corpus.".format(str(res[0][0])))

    def CollectTexts(self):
        """Get a list of texts from the database"""
        return Db.con.dictquery('SELECT title, transtitle, id from text_ids')

    def WordCounts_monoling(self):
        results = Db.con.dictquery('SELECT title, id from text_ids')
        texts=list()
        wctotal = 0 
        maxtitleLength = len('title')
        maxWcLength = len('word count')
        for res in results:
            #Fetch wordcount for each text and target text
            texts.append({'id':res['id'],'title':res['title'],'wordcount':self.wordCountForText(res['id'],Db.searched_table)})
            #Get string length information for the output table
            if len(res['title'])>maxtitleLength:
                maxtitleLength = len(res['title'])
            if len(texts[-1]['wordcount'])>maxWcLength:
                maxWcLength = len(texts[-1]['wordcount'])

        for text in texts:
            print('{0:3} | {1:{titlewidth}} | {2:{wcwidth}} '.format(text['id'],text['title'],text['wordcount'],text['translation title'],text['trwordcount'],
                titlewidth = maxtitleLength, wcwidth = maxWcLength))
            wctotal += text['wordcount']

        print('\nTOTAL: {} words.'.format(wctotal))

    def WordCounts(self):
        """Count words in the texts"""
        #This needs to be improved:
        tables = {'source':'fi_conll','target':'ru_conll'}
        #########
        maxtitleLength = len('title')
        maxWcLength = len('word count')
        max_trtitleLength = len('translation title')
        max_trWcLength = len('trans. word count')
        texts = list()
        print('Analyzing...')
        #Start printing data for each text and target text
        results = self.CollectTexts()
        for res in results:
            #Fetch wordcount for each text and target text
            texts.append({'id':res['id'],'title':res['title'],'wordcount':self.wordCountForText(res['id'],tables['source']),
                'translation title':res['transtitle'],'trwordcount':self.wordCountForText(res['id'],tables['target'])})
            #Get string length information for the output table
            if len(res['title'])>maxtitleLength:
                maxtitleLength = len(res['title'])
            if len(texts[-1]['wordcount'])>maxWcLength:
                maxWcLength = len(texts[-1]['wordcount'])
            if len(res['transtitle'])>max_trtitleLength:
                max_trtitleLength = len(res['transtitle'])
            if len(texts[-1]['trwordcount'])>max_trWcLength:
                max_trWcLength = len(texts[-1]['trwordcount'])
        #Print the output table
        print('{0:3} | {1:{titlewidth}} | {2:{wcwidth}} | {3:{trtitlewidth}} | {4:{trwcwidth}}'.format('Id','Title','Word count', 'Translation title', 'translation wordcount',
            titlewidth = maxtitleLength, wcwidth = maxWcLength, trtitlewidth = max_trtitleLength, trwcwidth = max_trWcLength))
        for text in texts:
            print('{0:3} | {1:{titlewidth}} | {2:{wcwidth}} | {3:{trtitlewidth}} | {4:{trwcwidth}}'.format(text['id'],text['title'],text['wordcount'],text['translation title'],text['trwordcount'],
                titlewidth = maxtitleLength, wcwidth = maxWcLength, trtitlewidth = max_trtitleLength, trwcwidth = max_trWcLength))
        #Print csv if the user wants to:
        csvmenu = multimenu({'y':'yes','n':'no'}, 'Write csv?')
        if csvmenu.answer == 'y':
            with open('wordcounts.csv','w') as f:
                fieldnames = ['id', 'title','wordcount','translation title','trwordcount']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for text in texts:
                    writer.writerow(text)


    def runmenu(self):
        #Clear the terminal:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.menu.prompt_valid()
        while self.menu.answer != 'c':
            self.evaluatestatmenu()
            self.menu.prompt_valid()

    def evaluatestatmenu(self):
        """choose what to do"""
        if self.menu.answer == '1':
            self.WordCounts()
        if self.menu.answer == '2':
            self.WordCounts_monoling()
        if self.menu.answer == '3':
            self.wordCountForAll(Db.searched_table)



##################################################

def printResults(thisSearch):
        if len(thisSearch.matches) >0:
            printcount = input('Found {} occurences. How many should I print? (press enter to print all)\n'.format(thisSearch.absolutematchcount))
            if printcount == '':
                printcount = thisSearch.absolutematchcount
            else:
                printcount = int(printcount)
            while printcount > thisSearch.absolutematchcount:
                printcount = int(input('Please give a number smaller than {}.'.format(thisSearch.absolutematchcount + 1)))
            ordermenu = multimenu({'r':'randomize','n':'Do not randomize'},'Should I randomize the order?')
            if ordermenu.answer =='r':
                randomkeys = random.sample(list(thisSearch.matches),printcount)
                printmatches = list()
                for rkey in randomkeys:
                    alignsegment = thisSearch.matches[rkey]
                    #randomly select 1 of the matches in this segment
                    printmatches.append(random.choice(alignsegment))
            else:
                printmatches = list()
                for align_id, matches in thisSearch.matches.items():
                    for match in matches:
                        if len(printmatches) < printcount:
                            printmatches.append(match)
                        else:
                            break
            #actual printing
            #========================================
            csvrows = list()
            rows = list()
            table = Texttable()
            #Initialize table printer
            table.set_cols_align(["l", "l"])
            table.set_cols_valign(["m", "m"])

            if thisSearch.isparallel:
                headerrow = ['sl','tl','source']
            else:
                headerrow = ['concordance','source']
            csvrows = [headerrow]

            for idx, match in enumerate(printmatches):
                match.BuildSlContext()
                if thisSearch.isparallel:
                    match.BuildTlContext()
                    rows.append(['Source text id: {}, Sentence id: {}, align id: {}\n'.format(match.matchedword.sourcetextid, match.matchedsentence.sentence_id, match.align_id), ''])
                    rows.append([get_color_string(bcolors.BLUE,match.slcontextstring), get_color_string(bcolors.RED,match.tlcontextstring)])
                    csvrows.append([match.slcontextstring,match.tlcontextstring,match.matchedword.sourcetextid])
                else:
                    if len(match.slcontextstring)>3000:
                        printedstring = match.matchedsentence.printstring + "(only sentence printed)"
                    else:
                        printedstring = match.slcontextstring
                    print('{}:\n=======================\n{}\n----------------------\n[Sentence id: {}, align id: {}, text_id: {}]\n\n\n'.format(idx,textwrap.fill(printedstring), match.matchedsentence.sentence_id, match.align_id,match.matchedword.sourcetextid))
                    csvrows.append([match.slcontextstring,match.matchedword.sourcetextid])
            if thisSearch.isparallel:
                table.add_rows(rows)
                print(table.draw() + "\n")
            #========================================
            csvmenu = multimenu({'y':'yes','n':'no'},'Save csv?',False)
            if csvmenu.answer == 'y':
                fname = input('Give the name of the csv:\n>')
                with open(fname, "w",newline='') as f:
                    writer = csv.writer(f)
                    try:
                        writer.writerows(csvrows)
                    except TypeError:
                        import ipdb; ipdb.set_trace()
        else:
            print('Sorry, nothing found.')
            print(thisSearch.subquery)
            print(thisSearch.subqueryvalues)


def resultprinter(matchitems,limit=1,parallel=False):
    """Print to screen the specified number of elements from search object"""
    printed = 0
    sentences = dict()
    for key, matches in matchitems:
        for match in matches:
            if printed == int(limit):
                break
            #match.monoConcordance()
            #match.matchedsentence.buildPrintString()
            match.BuildSlContext()
            if  parallel:
                match.BuildTlContext()
            printed += 1
            print('{}:\t{}\nSentence id: {}, align id: {}\n'.format(printed,match.matchedsentence.printstring, match.matchedsentence.sentence_id, key))
            #Save the sentence so it can be referenced easily
            sentences[str(printed)] = match.matchedsentence
    return sentences


def LoadCsv():
    """Load data from an external import csv file"""
    fname = input('Give the path of the file\n>')
    with open(fname, 'r') as f:
        valsfromfile = list(csv.reader(f))
    vals=list()
    for valfromfile in valsfromfile:
        vals.append(valfromfile[0])
    return vals

##################################################


#Start the menu

if __name__ == "__main__":
    searchmenu = MainMenu()
    while searchmenu.run == True:
        searchmenu.runmenu()
        if searchmenu.pause:
            input('Press enter to continue')
            searchmenu.pause=False
