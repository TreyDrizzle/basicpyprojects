import requests
import string
from bs4 import BeautifulSoup


Enter_input = input("Enter DOB(monthday i.e may1): ")

lookup = "https://www.famousbirthdays.com/" + Enter_input
url  = lookup + ".html"



def birthday_lookup(url):
    url_open =requests.get(url)
    soup = BeautifulSoup(url_open._content, 'html.parser')
    name = soup.find('div', {'class':'name'})

    print("The most famous person that has your birthday according to FamousBirthdays.com is:", name.text)


birthday_lookup(url)


