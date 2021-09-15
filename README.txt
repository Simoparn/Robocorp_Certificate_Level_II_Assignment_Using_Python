TABLE OF CONTENTS

    OVERVIEW

    INSTRUCTIONS

        LOCAL USE

            CHECK PACKAGES IN VISUAL STUDIO CODE
            IF USING ORIGINAL SELENIUM.WEBDRIVER
            CONFIGURE VAULT CREDENTIALS (USERNAME AND PASSWORD)
            DEFAULT USERNAME AND PASSWORD
            DOWNLOAD LINK FOR THE ORDERS FILE

        ROBOCORP CLOUD

    ABOUT COMMITS

    TODO

    BUGS

    ISSUES
        POSSIBLE ISSUES WITH RPA AND SELENIUM LIBRARIES


OVERVIEW
   
    Certificate level II, Simo Pärnänen (using Python to implement RPA Framework keywords),
    with an additional request for username and password credentials.  Saves the order HTML receipt as a PDF file. Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt. Creates ZIP archive of the
    receipts and the images.




INSTRUCTIONS

    LOCAL USE

    
        CHECK PACKAGES IN VISUAL STUDIO CODE  
            Terminal->py -m pip list

             Terminal->py -m pip install selenium


     IF USING ORIGINAL SELENIUM.WEBDRIVER

            Set the driver in your PATH.

            https://sites.google.com/chromium.org/driver/getting-started


        CONFIGURE VAULT CREDENTIALS (USERNAME AND PASSWORD)
            The vault.json file should be moved to root of the repository directory,
            Change the value of the RPA_SECRET_FILE attribute in devdata/env.json
            to ../vault.json for example. Change the username and password in vault.json.
        
            vault.json


            {
                "credentials": {
                "username": "username",
                "password": "password"
            }
        }


        DEFAULT USERNAME AND PASSWORD
            Username: "username", Password: "password"
    
        DOWNLOAD LINK FOR THE ORDERS FILE
            Orders file: https://robotsparebinindustries.com/orders.csv


    ROBOCORP CLOUD

        Remove the vault.json from the root directory and change the credentials according
        to your configured vault settings in Robocorp Cloud.

ABOUT COMMITS
    First commit is wrongly labeled as the 9th, because of faulty commit message
    from the previous repository.


TODO
    End Log still lacks implementation in Keywordsinpython.py

BUGS
    (10/09/2021) Wrong number of paramters for Order Robots From RobotSpareBin Industries Industries Inc?
                   

ISSUES

    POSSIBLE ISSUES WITH RPA AND SELENIUM LIBRARIES
        If the Python interpreter can't resolve the RPA and SELENIUM library in 
        keywordsinpython.py, I recommend copying the library folder to the Lib\site-packages folder of your 
        interpreter and reloading.   