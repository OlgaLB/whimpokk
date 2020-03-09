Feature: Select sound items for the custom combination

  Scenario: Select one sound item
     Given the user is on main page logged in to the account
      When user clicks Summer Night and Fireplace
      Then Save becomes available
      # And Summer Night becomes selected
      # And slidebar appears under the Summer Night image
      # And Fireplace becomes selected
      # And slidebar appears under the Fireplace image
      # And Favorites button is unavailable
      # And Share button becomes available
