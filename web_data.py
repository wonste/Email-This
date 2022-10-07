# We can analyze all of the data of the web page
# and with the extension on the browser we can update
# the measurements found. We will analyze Chrome
# since that is the most used browser.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas
import requests


def get_html_document(url):

    response = requests.get(url)

    return response.text
    # this returns our repsonse in json format


# Use selenium library to get the URL based on the web browser used
# In this case we are doing chrome to get the current URL
# LINE 28 NEEDS A CORRECT PATH THAT I DON'T KNOW WHAT IT IS -GREISY
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://google.com')
old_url = driver.current_url


class NewPage:

    def __init__(self, old_url):
        self.old_url = old_url

    def __call__(self, driver):
        if driver.current_url != self.old_url:
            return driver.current_url


while True:
    wait = WebDriverWait(driver, timeout=120)
    url_to_scrape = wait.until(NewPage(old_url))
    old_url = url_to_scrape

    print(url_to_scrape)

    # new url than before

    html_document = get_html_document(url_to_scrape)

    soup = BeautifulSoup(html_document, features='html.parser')

    # Creating empty list to hold the type of measurements being used by the page
    unit = []           # oz, ml, tbsp, tsp, L, cup(s) etc...
    amount = []

    page_content = driver.page_source
    the_soup = BeautifulSoup(page_content, features="html.parser")

    # Trying to find the keywords that will help us get the measurements in the page
    for e in soup.findAll(attrs={"class": "ingredients"}):
        the_amount = e.find('li', attr={'class': 'data-amount'})
        the_unit = e.find('li', attr={'class': 'data-unit'})




# now we need to check whether the measurements are generally imperial or metric and convert (and after that we will need to redisplay as the style the user prefers. )