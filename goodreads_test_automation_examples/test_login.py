from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import selectors
from Elements.elements import *
from goodreads_functions import *
import datetime

@pytest.mark.beforeLogin
def test_navigate():
    navigate_page(page_url)
    click_element(link_signIn)
    click_element(btn_signInWithGoogle)

@pytest.mark.beforeLogin
def test_login_with_valid_credentials():
    test_navigate()
    type_input(inputBox_email,input_email)
    click_element(inputBox_password)
    type_input(inputBox_password,input_password)
    click_element(btn_signIn)

    