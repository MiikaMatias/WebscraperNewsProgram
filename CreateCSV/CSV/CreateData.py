import sys
from traceback import print_tb
sys.path.append(r'C:\Users\Miika\Desktop\Python projects\Projects\WebscraperNewsProgram')

from cgi import print_arguments, test
import CreateCSV.Constants.Constants as c

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import requests 
import random
import time




#Takes all articles from the main page of Yle up to a certain point; returns them as a string convertible to csv
class Yle():

    def mainstories(soup,file):
            list = soup.find_all('li')
            for item in list:
                if not item.find('h3') == None:
                    headline = item.find('h3').text
                    link = item.find('a')
                    link = c.URL_YLE + link['href']
                    data = [c.INDEX, 'yleuutiset', str(link),str(headline)]
                    file.append(data)
                    c.INDEX += 1
            return file

    def data(file):
        op = webdriver.ChromeOptions()
        op.add_argument('--headless')
        browser = webdriver.Chrome(c.PATH_CHROMEDRIVER,options=op)
        browser.get(c.URL_YLE)
        browser.implicitly_wait(12)
        for i in range(5):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
        html_text = browser.execute_script("return document.body.innerHTML;")
        soup = BeautifulSoup(html_text,'lxml')
        file = Yle.mainstories(soup,file)
        return file

#Takes all articles from the main page of AP news up to a certain point; returns them as a string convertible to csv
class ApNews():
    
    def mainstories(soup,file): #takes all stories from ap landing, makes a csv file precursor that is written via writecsv(file)
        body = soup.find('div',class_ = 'Body') 
        landing = body.find('div',class_ = 'Landing')
        fluidwrapper = landing.find('div',class_='fluid-wrapper')
        stories = fluidwrapper.find('div', attrs={'data-key':True})
        storylist = stories.find_all('a',attrs={'data-key':True})
        for story in storylist:      #for loop of all stories in mainstories, append into file             
            if 'h2' in str(story): 
                from_url = c.URL_APNEWS + story['href']
                header = story.find('h2').text
                data = [c.INDEX,'apnews',str(from_url),str(header)]
                file.append(data)
                c.INDEX += 1

    def otherstories(soup,file):
        cards = soup.find('article', class_= 'cards')
        lists = cards.find_all('li')
        for item in lists:
            headline = item.find('h4')
            link = item.find('a')
            if not headline == None or not link == None:
                from_url = c.URL_APNEWS + link['href']
                header = headline.text
                data = [c.INDEX,'apnews',str(from_url),str(header)]
                file.append(data)
                c.INDEX+=1

    def data():
        op = webdriver.ChromeOptions()
        op.add_argument('--headless')
        browser = webdriver.Chrome(c.PATH_CHROMEDRIVER,options=op)
        browser.get(c.URL_APNEWS)
        browser.implicitly_wait(12)
        for i in range(5):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
        html_text = browser.execute_script("return document.body.innerHTML;")
        soup = BeautifulSoup(html_text,'lxml') 
        file = []
        ApNews.mainstories(soup,file)
        ApNews.otherstories(soup,file)
        file = Yle.data(file)
        return file
    