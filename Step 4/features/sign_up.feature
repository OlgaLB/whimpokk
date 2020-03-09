# Feature: Sign up

 # Scenario: open sign up dialog
    # Given the Noisli web site is opened #by https://www.noisli.com/ URL
     # When user clicks 'Sign Up' button
     # Then 'Sign Up, it's Free :)' dialog is opened
     # And 'Email address' edit box is available
     # And 'Password' edit box is available
     # And 'X' button is available
     # And 'log in' button is available
     # And '?' button is available
     # And 'Sign Up with Facebook' button is available
     # And 'Sign Up with Google' button is available
     # And 'Terms of Use' link is available

 # Scenario: create an account
    # Given the 'Sign Up, it's Free :)' dialog is opened
     # When user enters 'olytvynovabogdanova@gmail.com' to the 'Email address' edit box
     # And user enters '12345678' to the 'Email address' edit box
     # And user clicks the 'Sign Up, it's Free' button
     # Then 'Thanks for signing up!' dialog is opened
     # And 'Ok' button is available
     # And 'X' button is available

 # Scenario: close the 'Thanks for signing up!' window
    # Given the 'Thanks for signing up!' dialog is opened
     # When user clicks 'Ok' button
     # Then 'Thanks for signing up!' dialog is closed
     # And main page of Noisli web site is available
