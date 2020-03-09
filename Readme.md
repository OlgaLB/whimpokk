Welcome :)  
The following should be installed to run the solution:  
1) python  
examples of commands for Ubuntu (they might differ depending on your OS):  
sudo apt-get update  
sudo apt-get install python3.6  
2) pip  
sudo apt install python3-venv python3-pip  
3) behave  
sudo pip install git+https://github.com/behave/behave  
4) selenium  
sudo pip install selenium  
5) Mozilla Firebox web browser of the supported version  
6) geckodriver of the appropriate version  
wget https://github.com/mozilla/geckodriver/releases/download/v<version>/geckodriver-v<version>-linux64.tar.gz  
tar -xvzf geckodriver*  
chmod +x geckodriver  

Gecodriver should be added to the PATH:  
export PATH=$PATH:/<path-to-extracted-file>/  

Automated tests should be run from 'steps' folder by launching 'behave'.  

Example:  
$ behave  
Feature: Select sound items for the custom combination # ../create_custom_combination.feature:1  

Scenario: Select one sound item                           # ../create_custom_combination.feature:3  
Given the user is on main page logged in to the account # create_custom_combination.py:5 52.248s  
When user clicks Summer Night and Fireplace             # create_custom_combination.py:24 6.845s  
Then Save becomes available                             # create_custom_combination.py:38 5.427s  

Feature: Log in # ../log_in.feature:1  

Scenario: log in using profile                         # ../log_in.feature:3  
Given the Welcome Back :) dialog is opened           # log_in.py:5 7.378s  
When user enters valid credentials and clicks Log In # log_in.py:10 15.489s  
Then Set Timer button becomes available              # log_in.py:19 10.888s  

Feature: Open Welcome Back dialog # ../open_log_in.feature:1  

Scenario: open log in dialog          # ../open_log_in.feature:3  
Given the Noisli web site is opened # open_log_in.py:5 14.162s  
When user clicks Log In button      # open_log_in.py:10 15.480s  
Then Email edit box is available    # open_log_in.py:19 5.507s  

Feature: Open Noisli # ../open_site.feature:1  

Scenario: the Noisli web site is opened                                                   # ../open_site.feature:3  
When the Noisli web site is opened                                                      # open_site.py:5 18.391s  
Then it has a title Noisli - Improve Focus and Boost Productivity with Background Noise # open_site.py:10 5.535s  

Feature: Set Timer # ../set_timer.feature:1  

Scenario: Activate Start Timer button                                              # ../set_timer.feature:3  
Given the user is on main page logged in to the account with the sounds selected # set_timer.py:5 55.753s  
When user clicks Set Timer                                                       # set_timer.py:30 0.250s  
Then Start button becomes available                                              # set_timer.py:35 5.413s  

Feature: Start Timer # ../start_timer.feature:1  

Scenario: Start Timer                 # ../start_timer.feature:3  
Given the Set Timer button pressed  # start_timer.py:5 47.248s  
When user clicks Start              # start_timer.py:33 0.252s  
Then Pause button becomes available # start_timer.py:38 5.426s  

6 features passed, 0 failed, 0 skipped  
6 scenarios passed, 0 failed, 0 skipped  
17 steps passed, 0 failed, 0 skipped, 0 undefined  
Took 4m31.692s  
