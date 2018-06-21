#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium import webdriver  
from subprocess import Popen, PIPE
import time
import sys
import json
import re
import string
from get_korp_json import WebContent
from get_nkrja_json import Nkrja, CorpushtmlTostring, CrawlPages
import data.araneumdata.fi as fi
import data.araneumdata.ru as ru

class Araneum(Nkrja):

    def __init__(self, url, outfilename=None):
        if not 'viewmode=sen' in url:
            url += ';viewmode=sen'
        super().__init__('{};fromp='.format(url), 'araneum', outfilename)
        self.selenium = WebContent()
        self.selenium.Start()


    def GetContent(self):
        rows = self.soup.find('table',{'id':'conclines'}).findAll('tr')
        for row in rows:
            try:
                source = row.find('td',{'class':'ref'}).text
                conc = row.find('td',{'class':'par'}).text
                conc = conc.replace('<s>','')
                conc = conc.replace(r'</s>','')
                words = re.split('(\s+)',conc)
                text = CorpushtmlTostring(words)
                self.entries.append({'text':text,'source':source})
            except AttributeError:
                print('no td with class par found')
                return False
        return True

def GetData(query):
    if "filename" in query:
        crawler = Araneum(query['url'], query['filename'])
    else:
        crawler = Araneum(query['url'])
    crawler.GetUrl()
    crawler.GetContent()
    final = CrawlPages(crawler)
    return final


