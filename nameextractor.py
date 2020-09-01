from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib
import requests
import shutil
#from PIL import Image
#import PIL
import logging
from PIL import Image
from io import BytesIO
import os
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException
)
from selenium.webdriver.support.ui import WebDriverWait

def do():
    driver=webdriver.Chrome()
    driver.get("https://www.mobile.de/auto/")
    sleep(2)
    markenE=driver.find_elements_by_xpath('//a[contains(@class,"btn btn--link Link___3oByUb") and contains(@href,"/auto/")][not(contains(@href, "mobile.de"))]')
    urls=[]
    for i in markenE:
        urls.append(i.get_attribute("href"))
    links=[]
    print(urls)
    marken=[]
    models=[]
    for i in range(len(urls)):
        print(urls[i])
        driver.get(urls[i])
        sleep(2)
        modelElements=driver.find_elements_by_xpath('//a[contains(@href,"/auto/")][not(contains(@href, "mobile.de"))]')
        #print("yeet",modelElements)
        for i in range(len(modelElements)):
            models.append(modelElements[i].get_attribute("text"))
        #print(models)
        driver.get("https://www.mobile.de/auto/")
        sleep(2)
    print(models)
        
        
##    markenElements2=driver.find_elements_by_xpath('//a[@class="btn btn--link Link___3oByUb"]')
##    for j in range(len(markenElements2)):
##        marken.append(markenElements2[j].get_attribute("href").split("/")[4])
##    print(marken)

do()
