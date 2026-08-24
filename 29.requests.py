'''requests:
--requests module is used to send the HTTP request to the server
--get is used to retrieve the data
import requests
url_ = "https://books.toscrape.com/"
response = requests.get(url_)
print(response.status_code)

Beautifulsoup module:
--bs4 is version of the module,which is used to get the data from the website
'''
import requests
from bs4 import BeautifulSoup

url_ = "https://books.toscrape.com/"
response = requests.get(url_)
titl_=BeautifulSoup(response.text,'html.parser')
print(titl_)
'''
import requests
from bs4 import BeautifulSoup

url_ = "https://books.toscrape.com/"
response = requests.get(url_)
titl_ = BeautifulSoup(response.text,'html.parser')
books = titl_.find_all('h3')
for book in books:
    titl_ = book.find('a').get('title')
    print(titl_)

web scraping:
--The process of collecting data from the websites with normal python
program is called as web scraping
'''
