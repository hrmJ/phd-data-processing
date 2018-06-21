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
from sys import platform as _platform
import data.korpdata.fi as patterns
 
if _platform == "linux" or _platform == "linux2":
    scriptdir = '/home/juho/syntparsedmustikka'
    phddir = '/home/juho/phdmanuscript'
elif _platform == "cygwin":
    scriptdir = '/cygdrive/k/corpora/syntparsedmustikka'
    phddir = '/cygdrive/k/phdmanuscript'

sys.path.append(scriptdir)
sys.path.append(phddir)

from articles.katu2016 import searchutils
#https://korp.csc.fi/#?prequery_within=sentence&cqp=%5B%5D&corpus=klk_fi_2000,klk_fi_1999,klk_fi_1998,klk_fi_1997,klk_fi_1996,klk_fi_1995,klk_fi_1994,klk_fi_1993,klk_fi_1992,klk_fi_1991,klk_fi_1990,klk_fi_1989,klk_fi_1988,klk_fi_1987,klk_fi_1986,klk_fi_1985,klk_fi_1984,klk_fi_1983,klk_fi_1982,klk_fi_1981,klk_fi_1980,dma&lang=en&hpp=1000&sort=random&word_pic&search_tab=2&random_seed=9044708&search=cqp%7C%5Bword%20%3D%20%22viime%22%5D%5Bword%20%3D%20%22viikolla%7Cvuonna%7Cp%C3%A4ivin%C3%A4%7Ckuussa%7Cvuosina%7Ckuukausina%22%5D&page={}

class WebContent():

    def __init__(self):
        self.maxpages = None
        self.data = list()
        self.rawdata = list()

    def Reset(self):
        self.maxpages = None
        self.data = list()
        self.rawdata = list()

    def Start(self):
        try:
            profile = FirefoxProfile('/home/juho/.mozilla/firefox/mwad0hks.default')
        except FileNotFoundError:
            try:
                profile = FirefoxProfile('/home/juho/.mozilla/firefox/axli79rw.default')
            except FileNotFoundError:
                profile = FirefoxProfile('/home/juho/.mozilla/firefox/aqljl12x.default')
        self.browser = webdriver.Firefox(profile)  
        self.browser.implicitly_wait(3)
        print('Browser ready')

    def GetHtml(self, url):
        self.browser.get(url)  
        time.sleep(1)  
        html = self.browser.page_source
        return html

    def Stop(self):
        self.browser.quit()

    def SingInToKorp(self):
        self.browser.get('https://korp.csc.fi')
        #1. locate the settings button and click it
        link1 = self.browser.find_element_by_tag_name('svg')
        link1.click()
        #2. Locate the sign in button and click
        login_link = self.browser.find_element_by_xpath("//li[@id='login']/a")
        login_link.click()
        #3. fill in university details and click log in
        affil_input = self.browser.find_element_by_id("user_idp_iddtext")
        affil_input.click()
        affil_input.send_keys('University of Tampere')
        self.browser.find_element_by_tag_name("h1").click()
        self.browser.find_element_by_id("wayf_submit_button").click()
        #4. sign in to uta
        #usrname = input("Uta username:")
        #password = input("Uta password:")
        usrname = "jh89963"
        password = "9MVfwoiF891"
        usr = self.browser.find_element_by_id("username")
        usr.send_keys(usrname)
        passw = self.browser.find_element_by_id("password")
        passw.send_keys(password)
        subm = self.browser.find_element_by_xpath("//button[@type='submit']")
        subm.click()

    def OutputData(self):

        prefix = input('Give the prefix for the json files: ')
        for idx, data in enumerate(self.data):
            fname = "data/korpdata/{}_page{}.json".format(prefix, idx)
            print('Outputting ' + fname)
            try:
                searchutils.WriteJson(data, fname)
            except:
                print('Cant write {}'.format(fname))



def GetNextPage(thisbrowser, url, pageidx):
    """Get the next result page"""
    jsonprefix = "https://korp.csc.fi"
    if pageidx>0:
        url += "&page={}".format(pageidx)

    html = thisbrowser.GetHtml(url)
    if pageidx>0:
        maxrange = 1
        print('wait {} secs...'.format(maxrange))
        for tidx in range(1,maxrange):
            time.sleep(1)
            print(maxrange - tidx)

    soup = BeautifulSoup(html,'lxml')

    if not thisbrowser.maxpages:
        thisbrowser.maxpages = int(input('Anna tulossivujen enimmäismäärä:')) 

    jsonlink_sp = soup.find('a', id='json-link')
    stop = 0
    while not jsonlink_sp.get('ng-href'):
        html = thisbrowser.browser.page_source
        soup = BeautifulSoup(html,'lxml')
        jsonlink_sp = soup.find('a', id='json-link')
        stop += 1
        time.sleep(1)
        print('{}\n{}'.format(jsonlink_sp, stop))
        if stop % 5 ==0:
            #If stuck, try refreshing the browser
            thisbrowser.browser.refresh()
        if stop == 100:
            print('No luck!')
            break

    jsonlink = thisbrowser.browser.find_element(By.ID,value='json-link')
    try:
        jsonurl = jsonprefix + jsonlink_sp.get('ng-href')
        #rawjson = thisbrowser.GetHtml(jsonurl)
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = thisbrowser.browser.current_window_handle
        jsonlink.click()
        time.sleep(5)
        signin_window_handle = None
        while not signin_window_handle:
            for handle in thisbrowser.browser.window_handles:
                if handle != main_window_handle:
                    signin_window_handle = handle
                    break
        thisbrowser.browser.switch_to.window(signin_window_handle)
        rawjson = thisbrowser.browser.page_source

        thisbrowser.browser.close()
        thisbrowser.browser.switch_to.window(main_window_handle)

        sp = BeautifulSoup(rawjson)
        jsoncontent = sp.text
        jsondata = json.loads(jsoncontent)
        thisbrowser.data.append(jsondata)
        print('Succesfully loaded json of page {}'.format(pageidx))
        return True
    except AttributeError:
        print('Nothing found!')
        return False
    except ValueError:
        print('Failed to load json!')
        return jsonurl
    except:
        print('Unknown error!')
        return False

def StartKorp():
    b = WebContent()
    b.Start()
    b.SingInToKorp()
    return b


def GetData(thisbrowser, starturl):
    """Get the whole data set from korp import (i.e. all the pages)"""
    p = GetNextPage(thisbrowser, starturl, 0)
    pageidx = 1
    p = True 
    while p:
        if len(thisbrowser.data)>40 or pageidx > thisbrowser.maxpages:
            ##MAx 20000 entries! (40 * 500)
            break
        p = GetNextPage(thisbrowser, starturl, pageidx)
        pageidx += 1

    thisbrowser.OutputData()
    thisbrowser.maxpages=None


