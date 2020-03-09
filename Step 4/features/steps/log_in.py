from behave import *
from selenium import webdriver
import time

@given('the Welcome Back :) dialog is opened')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://www.noisli.com/')

@when('user enters valid credentials and clicks Log In')
def step_impl(context):
    time.sleep(10)
    element = context.browser.find_element_by_link_text("skip")
    element.click() 
    time.sleep(5)
    element = context.browser.find_element_by_id('login-span')
    element.click()

@then('Set Timer button becomes available')
def step_impl(context):
    element = context.browser.find_element_by_id('login-modal-input-email')
    element.send_keys('olytvynovabogdanova@gmail.com') 
    element = context.browser.find_element_by_id('login-modal-input-password')
    element.send_keys('12345678') 
    time.sleep(5)
    element = context.browser.find_element_by_id('login-modal-input-submit')
    element.click() 
    element = context.browser.find_element_by_id("set-timer-span") 
    # TO DO: check Favorites button becomes available
    # TO DO: check Settings button becomes available
    # TO DO: check Favorite Combos button becomes available
    # TO DO: check Timer button becomes available
    # TO DO: check Text editor button becomes available
    # TO DO: check Welcome Back :) dialog is closed
    # TO DO: check Log in button becomes invisible
    # TO DO: check ? button becomes invisible
    # TO DO: check Sign up button becomes invisible
    time.sleep(5)
    context.browser.quit()
