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

<<<<<<< HEAD
def getID(url):
    pUrl = urlparse.urlparse(url)
    return urlparse.parse_qs(pUrl.query)['in']['0']


=======
>>>>>>> dff1d21d3e194f732bffa90327b6afa455d6224f

def ViewBot(driver):
    visited = {}
    pList = []
    count = 0
    while True:
            #sleep to make sure everthing loads.
            #add random to make us look human. 
<<<<<<< HEAD
            time.sleep(random.uniform(3.5,6.9))
            page = BeautifulSoup(driver.page_source)
            people = getPeopleLinks(page)


=======
            time.sleep(1)
            driver.get("https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&sid=Zu)")
            time.sleep(1)
            
            all_buttons = driver.find_element(By.TAG_NAME, 'button')
            connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

            for btn in connect_buttons:
                driver.execute_script("arguments[0].click();", btn)


            
>>>>>>> dff1d21d3e194f732bffa90327b6afa455d6224f
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

<<<<<<< HEAD
    os.system("cls")
    print; "[+] Success! logged into Linkedin"
    ViewBot(driver)
    driver.close()

=======
    os.system('cls')
    ViewBot(driver)
    

   
>>>>>>> dff1d21d3e194f732bffa90327b6afa455d6224f
if __name__ == '__main__':
        Main()
   


