#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs
import re
import string
import sys
from sys import platform as _platform
import random
import textwrap
import data.nkrjadata.ru as patterns

class Nkrja():

    def __init__(self, starturl, crawlertype='nkrja', outfilename = None):
        self.crawlertype = crawlertype
        self.starturl = starturl
        if crawlertype == 'araneum':
            self.pageidx = 1
            self.currenturl = starturl + str(self.pageidx)
        elif crawlertype == 'nkrja':
            self.pageidx = 0
            self.currenturl = starturl
            self.itemidx = 1
        #mikä ol-tägi nkrj-tuloksissa
        self.entries = list()
        self.outfilename = outfilename

    def GetUrl(self):
        if self.crawlertype == 'nkrja':
            self.html = urlopen(self.currenturl)
        elif self.crawlertype == 'araneum':
            self.html = self.selenium.GetHtml(self.currenturl)
        print('\t\turl retrieved')
        self.soup = BeautifulSoup(self.html,'lxml')
        print('\t\tsouped.')

    def GetTestHtml(self):
        with open('data/nkrjadata/test.html','r') as f:
            self.html = f.read()
        self.soup = BeautifulSoup(self.html,'lxml')

    def GetContent(self):
        ol = self.soup.find("ol",{"start": str(self.itemidx)})

        if not ol:
            #If the last page of the results was reached
            return False

        listitems = ol.findAll('li',recursive=False)
        for listitem in listitems:
            rawtext = listitem.find("ul").find("li").getText()
            exp = re.compile('(^[^\[]+)(\[[^\]]+\])(.*$)',re.MULTILINE)
            separated = exp.search(rawtext)
            if separated:
                words = re.split('(\s+)',separated.groups()[0])
                source = separated.groups()[1]
                text = CorpushtmlTostring(words)
                self.entries.append({'text':text,'source':source})

        return True

    def OutputContent(self):
        contents = ''
        sources = ''
        separator = '\n' + '!'*4 + '\n'

        for idx, entry in enumerate(self.entries):
            if idx < len(self.entries)-1:
                contents += entry['text'] + separator 
                sources += entry['source'] + '\n'
            else:
                contents += entry['text']
                sources += entry['source']

        if not self.outfilename:
            self.outfilename = input('Please give a filename: ')
        with open('data/' + self.crawlertype + 'data/' + self.outfilename + '.txt', 'w') as f:
            f.write(contents)
        with open('data/' + self.crawlertype + 'data/' + self.outfilename + '.sources.txt', 'w') as f:
            f.write(sources)

    def GetNextPage(self):
        """Get the next result page"""
        #100 here means that nkrja is set up so that it prints 100 results per page
        #this is contolled by the dpp parametr in the url
        self.pageidx += 1
        if self.crawlertype == 'nkrja':
            self.itemidx += 100
            self.currenturl = self.starturl + "&p=" + str(self.pageidx)
        elif self.crawlertype == 'araneum':
            self.currenturl = self.starturl + str(self.pageidx)
        hasresult = self.GetUrl()
        return self.GetContent()

def CorpushtmlTostring(words):
    nonwswords = list()
    for idx, word in enumerate(words):
        if not re.match('^\s+$',word) and word:
            nonwswords.append(word)
            
    return BuildString(nonwswords)

def BuildString(words):
    """Constructs a printable sentence"""
    printstring = ''
    isqmark = False
    #POISTA NONE-arvon saaneet sanat:
    words = list(filter(None.__ne__, words))
    for idx, word in enumerate(words):
        spacechar = ' '
        if idx>0:
            previous_word = words[idx-1]
            #if previous tag is a word:
            if  previous_word not in string.punctuation:
                #...and the current tag is a punctuation mark. Notice that exception is made for hyphens, since in mustikka they are often used as dashes
                if word in string.punctuation and word != '-':
                    #..don't insert whitespace
                    spacechar = ''
                    #except if this is the first quotation mark
                    if word == '\"' and not isqmark:
                        isqmark = True
                        spacechar = ' '
                    elif word == '\"' and isqmark:
                        isqmark = False
                        spacechar = ''
            #if previous tag was not a word
            elif previous_word in string.punctuation:
                #...and this tag is a punctuation mark
                if (word in string.punctuation and word != '-' and word != '\"') or isqmark:
                    #..don't insert whitespace
                    spacechar = ''
                if previous_word == '\"':
                    spacechar = ''
                    isqmark = True
                else:
                    spacechar = ' '
        else:
            #if this is the first word
            spacechar = ''

        printstring += spacechar + word

    return printstring

def GetData(query):
    if "filename" in query:
        crawler = Nkrja(query['url'], crawlertype='nkrja', outfilename=query['filename'])
    else:
        crawler = Nkrja(query['url'])
    crawler.GetUrl()
    crawler.GetContent()
    try: 
        final = CrawlPages(crawler)
    except:
        print('ERROR encountered. Trying to output...')
        crawler.OutputContent()

    return final


def CrawlPages(crawler):
    lastentries = len(crawler.entries)
    maxentries = 21000
    try:
        while crawler.GetNextPage():
            print('Adding page {}, total {} entries now collected. Example from the last entry:\n\n {}'.format(crawler.pageidx,len(crawler.entries),crawler.entries[-1]['text']))
            if lastentries == len(crawler.entries):
                #hacky
                break
            if len(crawler.entries) > maxentries:
                #Stop executing if found too much
                break
            lastentries = len(crawler.entries)
    except KeyboardInterrupt:
        return crawler

    print('Done. Extracted {} entries'.format(len(crawler.entries)))

    crawler.OutputContent()

    return crawler



