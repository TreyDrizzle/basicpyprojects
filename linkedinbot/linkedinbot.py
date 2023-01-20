import argparse, os, time
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

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

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="Linkedin email")
    parser.add_argument("password", help="linkedin password")
    args = parser.parse_args()

    browser = webdriver.Chrome()
    browser.get("https://www.linkedin.com/login")

    emailElement = browser.find_element_by_id("username")
    emailElement.send_keys(args.email)
    passElement = browser.find_element_by_id("password")
    passElement.send_keys(args.password)
    passElement.submit()

    os.system('cls')
    print ;"[+] Success! Linked in Bot has logged in"
    ViewBot(browser)
    browser.close()

if __name__ == '__main__':
        Main()


