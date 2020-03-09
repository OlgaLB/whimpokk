# Feature: Save custom combination

  # Scenario: Activate name entering for the combination to be saved
    # Given the user is on main page logged in to the account with the desired sound items selected
     # When user clicks 'Save'
     # Then edit box for the combination name is available
     # And a slidebar under the 'Fireplace' becomes visible
     # And 'Save' button becomes invisible
     # And 'Share' button becomes invisible

  # Scenario: Save the combination
    # Given the 'Save' button clicked
     # When user enters 'Fire & Night'
     # And presses Enter on the keyboard
     # Then the edit box for the combination name becomes invisible
     # And 'Fire & Night' button becomes visible and active
     # And 'Saved' label appears near the 'Favorite Combos' button
     # And 'Favorite Combos' button becomes selected

  # Scenario: Check the saved combination
    # Given the combination is saved
     # When user clicks 'Favorite Combos'
     # Then 'FAVORITE COMBOS' page is opened
     # And 'Fire & Night' button is visible and active
     # And 'Edit Menu' button is visible and active
     # And 'Save Combo' button is visible and inactive
     # And next 'Save Combo' button is visible and inactive
     # And next 'Save Combo' button is visible and inactive
     # And next 'Save Combo' button is visible and inactive
