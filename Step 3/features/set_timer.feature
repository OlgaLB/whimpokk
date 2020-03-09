Feature: Set Timer

  Scenario: Activate Start Timer button
     Given the user is on main page logged in to the account with the sounds selected
      When user clicks Set Timer
      Then Start button becomes available
      # And edit box with time becomes available
      # And Pause button becomes visible
      # And Fade out button becomes available
