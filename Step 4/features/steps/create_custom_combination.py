from behave import *
from selenium import webdriver
import time

@given('the user is on main page logged in to the account')
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

@when('user clicks Summer Night and Fireplace')
def step_impl(context):
    #loggedIn = context.browser.find_element_by_id('logged_in')
    #mainModule = loggedIn.find_element_by_id('main-module')
    #players = mainModule.find_element_by_id('players')
    #images = context.browser.find_element_by_tag_name("img")
    #image_element = context.browser.find_elements_by_xpath("//*[@id=\"players\"]/div[2]/img")
    element = context.browser.find_element_by_link_text("Accept")
    element.click()
    image_element = context.browser.find_elements_by_xpath("//div[@class='col-lg-3 col-md-3 col-sm-4 col-xs-6 text-center']/img[@data-name=\"summernight\"]")
    image_element[0].click()
    image_element = context.browser.find_elements_by_xpath("//div[@class='col-lg-3 col-md-3 col-sm-4 col-xs-6 text-center']/img[@data-name=\"fire\"]")
    image_element[0].click()
    
@then('Save becomes available')
def step_impl(context):
    element = context.browser.find_element_by_id('menu-dashboard-span-save')
    # TO DO: check the Summer Night becomes selected
    # TO DO: check the slidebar appears under the Summer Night image
    # TO DO: check the Fireplace becomes selected
    # TO DO: check the slidebar appears under the Fireplace image
    # TO DO: check the Favorites button is unavailable
    # TO DO: check the Share button becomes available
    time.sleep(5)
    context.browser.quit()
