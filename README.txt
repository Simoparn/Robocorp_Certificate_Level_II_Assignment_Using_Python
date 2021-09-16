TABLE OF CONTENTS

    OVERVIEW

    INSTRUCTIONS

        LOCAL USE

            CHECK PACKAGES IN VISUAL STUDIO CODE AND LOCAL FOLDERS
            IF USING ORIGINAL SELENIUM.WEBDRIVER
            CONFIGURE VAULT CREDENTIALS (USERNAME AND PASSWORD)
            DOWNLOAD LINK FOR THE ORDERS FILE

        ROBOCORP CLOUD

    ABOUT COMMITS

    TODO

    BUGS

    ISSUES
        POSSIBLE ISSUES WITH RPA AND SELENIUM LIBRARIES
        PROBLEM WITH RPA.ROBOCORP.VAULT


OVERVIEW
   
    Certificate level II, Simo Pärnänen (using Python to implement RPA Framework keywords),
    with an additional request for username and password credentials.  Saves the order HTML receipt as a PDF file. Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt. Creates ZIP archive of the
    receipts and the images.

    Check instructions for local testing configuration.




INSTRUCTIONS

    LOCAL USE

    
        CHECK PACKAGES IN VISUAL STUDIO CODE AND LOCAL FOLDERS
            Terminal->py -m pip list

            Terminal->py -m pip install selenium

            Folders:

            Users\AppData\Local\Programs\Python\Python39\Lib\site-packages


        IF USING ORIGINAL SELENIUM.WEBDRIVER

            Set the driver in your PATH.

            https://sites.google.com/chromium.org/driver/getting-started


        CONFIGURE VAULT CREDENTIALS (USERNAME AND PASSWORD)
           
           
           https://robocorp.com/docs/development-guide/variables-and-secrets/vault
           
           
           devdata/env.json

            {
            "RPA_SECRET_MANAGER": "RPA.Robocorp.Vault.FileSecrets",
            "RPA_SECRET_FILE": "/Users/<your-username-here>/vault.json"
            }
           

            Create a vault.json file to the root of the repository directory,
            Change the value of the RPA_SECRET_FILE attribute in devdata/env.json
            to ../vault.json for example. Change the username and password in vault.json.
        
            vault.json


            {
                "credentials": {
                "username": "username",
                "password": "password"
            }
        }

    
        DOWNLOAD LINK FOR THE ORDERS FILE
            Orders file: https://robotsparebinindustries.com/orders.csv


    ROBOCORP CLOUD

        Remove devdata/env.json and vault.json from the root directory and change the credentials according
        to your configured vault settings in Robocorp Cloud.

ABOUT COMMITS
    First commit is wrongly labeled as the 9th, because of faulty commit message
    from the previous repository.


TODO
    -End Log still lacks implementation in Keywordsinpython.py
    -Try using Robocorp Lab for RPA.Robocorp.Vault

BUGS
    (10/09/2021) Wrong number of paramters for Order Robots From RobotSpareBin Industries Industries Inc?
                   

ISSUES

    POSSIBLE ISSUES WITH RPA AND SELENIUM LIBRARIES
        If the Python interpreter can't resolve the RPA and SELENIUM library in 
        keywordsinpython.py, I recommend copying the library folder to the  
        Users\AppData\Local\Programs\Python\Python39\Lib\site-packages folder of your 
        interpreter and reloading.

    PROBLEM WITH RPA.ROBOCORP.VAULT  
        The package wasn't found through the VS Code extension. 
