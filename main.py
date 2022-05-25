from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import time

search = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
search.get('https://google.com')
search.find_element_by_name("q").send_keys("UNASP")
search.find_element_by_name("btnK").submit()
search.find_element_by_css_selector('div.yuRUbf > a').click()
search.find_element_by_css_selector('a.cc-ALLOW').click()
search.find_element_by_css_selector('a#slider-135-slide-284-layer-28').click()
search.find_element_by_xpath('//*[@id="listaDeCursosAncora"]/div/div/div[2]/a[1]').click()
search.find_element_by_css_selector('body > div.una-page > div.una-summary.full-width > div.container > div > div:nth-child(2) > div > div > a:nth-child(3)').click()
time.sleep(100)