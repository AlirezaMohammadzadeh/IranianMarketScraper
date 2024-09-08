from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
import requests
import convert_numbers
import time
import pandas as pd
from bs4 import BeautifulSoup 
from selenium.common.exceptions import NoSuchElementException
import os
from datetime import datetime
import random
import re


class WebScraper:
    def __init__(self, driver_path, options=None):
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        
        

    def stop_driver(self):
        if self.driver:
            self.driver.quit()


    def scrape_data(self,url,counter=0):
        if not self.driver:
            raise Exception("Driver not started. Call start_driver() before scraping data.")
        try:
            self.driver.get(url)
            time.sleep(5)
        except Exception as e:
            print(f'An error occured while trying get data by chrome driver : {str(e)}')
            return 0


    def scrape_by_Xpath(self, xpath):
        data = self.driver.find_element(by = By.XPATH,value = xpath)
        if data == None:
            raise Exception("Could scrape data by xpath")
        else:
            return data


    def scrape_by_class_name(self,class_name):
        data = self.driver.find_element(By.CLASS_NAME, class_name)
        if data == None:
            raise Exception("Could scrape data by class name")
        else:
            return data 

    
    def click_by_Xpath(self, xpath):
        try:
            self.driver.find_element(by = By.XPATH,value = xpath).click()
        except Exception as e:
            pass


    def scrape_by_tag_name(self,tag_name):
        try:
            data = self.driver.find_elements(By.TAG_NAME, tag_name)
            return data
        except Exception as e:
            pass

    
    def scrape_by_css_selector(self,css_selector):
        try:
            data = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            return data
        except Exception as e:
            pass

        
    def scrape_by_name(self,name):
        try:
            data = self.driver.find_element(By.NAME, name)
            return data
        except Exception:
            pass

