import argparse, os, time
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import parse_qsl, urljoin, urlparse

def getPeopleLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
                if '/in' in url:
                    links.append(url)
    return links

def getJobLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
                if '/jobs' in url:
                    links.append(url)
    return links

def getID(url):
    pUrl = urlparse.urlparse(url)
    return urlparse.parse_qs(pUrl.query)['in']['0']



def ViewBot(driver):
    visited = {}
    pList = []
    count = 0
    while True:
            #sleep to make sure everthing loads.
            #add random to make us look human. 
            time.sleep(random.uniform(3.5,6.9))
            page = BeautifulSoup(driver.page_source)
            people = getPeopleLinks(page)


def Main():
    
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    driver.implicitly_wait(3)

    username = driver.find_element(By.NAME, 'session_key')
    password = driver.find_element(By.NAME, 'session_password')
    login = driver.find_element(By.XPATH, '//button[1]')

    username.send_keys('tcdavissies@gmail.com')
    password.send_keys('linkbot')
    login.click()

    os.system("cls")
    print; "[+] Success! logged into Linkedin"
    ViewBot(driver)
    driver.close()

if __name__ == '__main__':
        Main()
   


