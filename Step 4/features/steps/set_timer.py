from behave import *
from selenium import webdriver
import time

@given('the user is on main page logged in to the account with the sounds selected')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://www.noisli.com/')
    time.sleep(10)
    element = context.browser.find_element_by_link_text("skip")
    element.click() 
    time.sleep(5)
    element = context.browser.find_element_by_id('login-span')
    element.click()
    element = context.browser.find_element_by_id('login-modal-input-email')
    element.send_keys('olytvynovabogdanova@gmail.com') 
    element = context.browser.find_element_by_id('login-modal-input-password')
    element.send_keys('12345678') 
    time.sleep(5)
    element = context.browser.find_element_by_id('login-modal-input-submit')
    element.click()  
    time.sleep(15)
    element = context.browser.find_element_by_link_text("Accept")
    element.click()
    image_element = context.browser.find_elements_by_xpath("//div[@class='col-lg-3 col-md-3 col-sm-4 col-xs-6 text-center']/img[@data-name=\"summernight\"]")
    image_element[0].click()
    image_element = context.browser.find_elements_by_xpath("//div[@class='col-lg-3 col-md-3 col-sm-4 col-xs-6 text-center']/img[@data-name=\"fire\"]")
    image_element[0].click()

@when('user clicks Set Timer')
def step_impl(context):
    element = context.browser.find_element_by_id("set-timer-span")
    element.click()
    
@then('Start button becomes available')
def step_impl(context):
    element = context.browser.find_element_by_id('start-span')
    # TO DO: check edit box with time becomes available
    # TO DO: check Pause button becomes visible
    # TO DO: check Fade out button becomes available
    time.sleep(5)
    context.browser.quit()
