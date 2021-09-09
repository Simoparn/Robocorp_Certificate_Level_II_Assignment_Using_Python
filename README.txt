TABLE OF CONTENTS

    OVERVIEW

    INSTRUCTIONS
        CHECK PACKAGES IN VISUAL STUDIO CODE
        DOWNLOAD LINK FOR THE ORDERS FILE
        POSSIBLE ISSUES WITH RPA LIBRARY


OVERVIEW
   
    Certificate level II, Simo Pärnänen (using Python). Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot. Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.




INSTRUCTIONS
    
    CHECK PACKAGES IN VISUAL STUDIO CODE  
        Terminal->py -m pip list


    DOWNLOAD LINK FOR THE ORDERS FILE
        Orders file: https://robotsparebinindustries.com/orders.csv


    POSSIBLE ISSUES WITH RPA LIBRARY
        If the Python interpreter can't resolve the RPA library in keywordsinpython.py,
        I recommend copying the library folder to the Lib\site-packages folder of your 
        interpreter.   