# We can analyze all of the data of the web page
# and with the extension on the browser we can update
# the measurements found. We will analyze Chrome
# since that is the most used browser.

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas

def getHTMLdocument(url):

    response = requests.get(url)

    return response.text
    # this returns our repsonse in json format

url_to_scrape = "NEED CURRENT/BROWSER TAB/URL"

html_document = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

# now we need to check whether the measurements are generally imperial or metric and convert (and after that we will need to redisplay as the style the user prefers. )