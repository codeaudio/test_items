from selenium import webdriver
import time, pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"                                                                                 

class TestFacebook(): 
    
    def test_auth(self, browser):                                                                                  
        browser.get(link) 
        assert browser.find_element_by_css_selector('.btn-add-to-basket')
