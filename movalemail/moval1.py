import re
import requests 
from bs4 import BeautifulSoup




url = "https://www.moval.edu/faculty-staff/"

# def email_lookup(url):
#     url_open =requests.get(url)
#     soup = BeautifulSoup(url_open._content, 'html.parser')
#     for link in soup.find_all('a',{'class':'email'}):
#         mailto = link.get('href')
#         email = mailto.replace("mailto:", "")
#         print(email)
            
# email_lookup(url)

def find_division(url):
    url_open =requests.get(url)
    soup = BeautifulSoup(url_open._content, 'html.parser')
    for link in soup.find_all('tr'):
        
        print(link.text)

find_division(url)
