# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:46:34 2020

@author: KOTIRMA
"""

from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

#Install chrome web driver

PATH = "path to chrome web driver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.lujakunto.fi/")
search = driver.find_element_by_id("product_search_words")

search.send_keys("oxdog ultralight 96")
search.send_keys(Keys.RETURN)

products = driver.find_elements_by_class_name("tc_product_mosaic")
    for product in products:
        product_name = driver.find_elements_by_class_name("product_mosaic_item_title")
        print(product_name.text)

    

#close the tab
driver.quit()






