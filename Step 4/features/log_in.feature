Feature: Log in

  Scenario: log in using profile
     Given the Welcome Back :) dialog is opened
      When user enters valid credentials and clicks Log In
      Then Set Timer button becomes available
      # And Favorites button becomes available
      # And Favorite Combos button becomes available
      # And Settings button becomes available
      # And Timer button becomes available
      # And Text editor button becomes available
      # And Welcome Back :) dialog is closed
      # And Log in button becomes invisible
      # And ? button becomes invisible
      # And Sign up button becomes invisible
