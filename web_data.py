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

# Use selenium library to get the URL based on the web browser used
# In this case we are doing chrome to get the current URL
driver = webdriver.Chrome()
the_url = driver.current_url

# Creating empty list to hold the type of measurements being used by the page
unit = []           # oz, ml, tbsp, tsp, L, cup(s) etc...
amount = []

driver.get(the_url)

page_content = driver.page_source
the_soup = BeautifulSoup(page_content)

# Trying to find the keywords that will help us get the measurements in the page
for e in soup.findAll(attrs={"class": "ingredients"}):
    the_amount = e.find('div', attr={'class': 'ingredients'})



# now we need to check whether the measurements are generally imperial or metric and convert (and after that we will need to redisplay as the style the user prefers. )