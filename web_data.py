# We can analyze all of the data of the web page
# and with the extension on the browser we can update
# the measurements found. We will analyze Chrome
# since that is the most used browser.

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

measurement_type = []
amount = []

