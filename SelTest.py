# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:11:47 2019

@author: Harshu
"""

import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname("C:\\ProgramData\\Anaconda3")
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.vehicleenquiry.service.gov.uk/")

# get the search textbox
search_field = driver.find_element_by_name("Vrm")

# enter search keyword and submit
search_field.send_keys("YA52MPV")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
search_field2= driver.find_element_by_css_selector("input[type='radio'][value='True']")
search_field2.click()
search_field2.submit()

element1=driver.page_source
print (element1)

pattern1 = re.search('\"CO2EmissionShown\"\>.*\<',element1)

print (pattern1)
# get the number of elements found
#print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search
#
#i=0
#for listitem in lists:
#   print (listitem.get_attribute("innerHTML"))
 #  i=i+1
  # if(i>10):
   #   break

# close the browser window
driver.quit()