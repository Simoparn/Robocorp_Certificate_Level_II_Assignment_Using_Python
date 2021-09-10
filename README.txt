TABLE OF CONTENTS

    OVERVIEW

    INSTRUCTIONS
        CHECK PACKAGES IN VISUAL STUDIO CODE
        DOWNLOAD LINK FOR THE ORDERS FILE

    ABOUT COMMITS

    ISSUES
        POSSIBLE ISSUES WITH RPA AND SELENIUMLIBRARY LIBRARIES


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
    Commits are labeled starting from 9, because of faulty commit message
    from the previous repository.

ISSUES

    POSSIBLE ISSUES WITH RPA AND SELENIUMLIBRARY LIBRARIES
        If the Python interpreter can't resolve the RPA and SELENIUMLIBRARY library in 
        keywordsinpython.py, I recommend copying the library folder to the Lib\site-packages folder of your 
        interpreter and reloading.   