import re
import requests 
from bs4 import BeautifulSoup




url = "https://www.moval.edu/faculty-staff/"

def email_lookup(url):
    url_open =requests.get(url)
    soup = BeautifulSoup(url_open._content, 'html.parser')
    
    for link in soup.find_all('a',{'class':'email'}):
        print(link.get('href'))
    
   
         
email_lookup(url)



