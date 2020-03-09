from behave import *
from selenium import webdriver
import time

@given('the Noisli web site is opened')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://www.noisli.com/')

@when('user clicks Log In button')
def step_impl(context):
    time.sleep(10)
    element = context.browser.find_element_by_link_text("skip")
    element.click() 
    time.sleep(5)
    element = context.browser.find_element_by_id('login-span')
    element.click()

@then('Email edit box is available')
def step_impl(context):
    element = context.browser.find_element_by_id('login-modal-input-email')
    # TO DO: check Password edit box is available
    # TO DO: check Log in button is available
    # TO DO: check Welcome Back :) dialog is active
    # TO DO: check Sign in with Facebook button becomes available
    # TO DO: check Sign in with Google button becomes available
    # TO DO: check X button becomes available
    # TO DO: check Create an Account button becomes available
    # TO DO: check Forgot password? button becomes available
    time.sleep(5)
    context.browser.quit()
