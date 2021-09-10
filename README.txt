TABLE OF CONTENTS

    OVERVIEW

    INSTRUCTIONS
        CHECK PACKAGES IN VISUAL STUDIO CODE
        DOWNLOAD LINK FOR THE ORDERS FILE

    ABOUT COMMITS

    TODO

    BUGS

    ISSUES
        POSSIBLE ISSUES WITH RPA AND SELENIUM LIBRARIES


OVERVIEW
   
    Certificate level II, Simo Pärnänen (using Python to implement RPA Framework keywords). 
    Saves the order HTML receipt as a PDF file. Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt. Creates ZIP archive of the
    receipts and the images.




INSTRUCTIONS
    
    CHECK PACKAGES IN VISUAL STUDIO CODE  
        Terminal->py -m pip list


    DOWNLOAD LINK FOR THE ORDERS FILE
        Orders file: https://robotsparebinindustries.com/orders.csv


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