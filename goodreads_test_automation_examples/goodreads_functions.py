from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import datetime


@pytest.fixture(scope='session', autouse=True)
def create_driver():
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    

def navigate_page(url):
    driver.get(url)
    
def click_element(selector_value):
    driver.find_element(By.XPATH,selector_value).click()
    
def type_input(selector_value,text):
    driver.find_element(By.XPATH,selector_value).send_keys(text)
    
def get_text_value(selector_value):
    return driver.find_element(By.XPATH,selector_value).text

def get_content(selector_value):
    return driver.find_element(By.XPATH,selector_value).get_attribute('content')
    




















