from behave import *
from selenium import webdriver
import time

@when('the Noisli web site is opened')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://www.noisli.com/')

@then('it has a title Noisli - Improve Focus and Boost Productivity with Background Noise')
def step_impl(context):
    assert context.browser.title == 'Noisli - Improve Focus and Boost Productivity with Background Noise'
     # TO DO: check Sign up button is available
     # TO DO: check Log in button is available
     # TO DO: check ? button is available
     # TO DO: check Mute button is available
     # TO DO: check Rain button is available
     # TO DO: check Thunderstorm button is available
     # TO DO: check Wind button is available
     # TO DO: check Forest button is available
     # TO DO: check Leaves button is available
     # TO DO: check Water stream button is available
     # TO DO: check Seaside button is available
     # TO DO: check Water button is available
     # TO DO: check Fireplace button is available
     # TO DO: check Summer night button is available
     # TO DO: check Coffee shop button is available
     # TO DO: check Train button is available
     # TO DO: check Fan button is available
     # TO DO: check White noise night button is available
     # TO DO: check Pink noise button is available
     # TO DO: check Brown noise button is available
     # TO DO: check Random button is available
     # TO DO: check Productivity button is available
     # TO DO: check Relax button is available
     # TO DO: check CREATE ACCOUNT button is available
     # TO DO: check Sign up button is available
     # TO DO: check Noisli button is available
     # TO DO: check IMPRINT button is available
     # TO DO: check APPS button is available
     # TO DO: check JOBS button is available
     # TO DO: check BLOG button is available
     # TO DO: check FEATURES button is available
     # TO DO: check TERMS & PRIVACY button is available
     # TO DO: check CONTACT button is available
    time.sleep(5)
    context.browser.quit()
