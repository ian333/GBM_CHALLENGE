import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class GooglePage(object):

    def __init__(self,driver):
        self._driver=driver
        self._url='https://google.com'
        self.search_locator='q'
    
    @property
    def is_loaded(self):
        WebDriverWait(self._driver,10).until(EC.presence_of_element_located((By.NAME,'q')))
        return True
    @property
    def keyword(self):
        input_field= self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    def open(self):
         