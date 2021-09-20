# -*- coding: utf-8 -*-
*** Settings ***
Documentation   Certificate level II, Simo Pärnänen (using Python).
...             Saves the order HTML receipt as a PDF file.
...             Saves the screenshot of the ordered robot.
...             Embeds the screenshot of the robot to the PDF receipt.
...             Creates ZIP archive of the receipts and the images.
Library         RPA.Browser.Selenium
Library         RPA.Tables
Library         RPA.FileSystem
Library         RPA.HTTP
Library         RPA.PDF
Library         RPA.Excel.Files
Library         RPA.Archive
Library         RPA.Robocloud.Secrets
Library         RPA.Dialogs
#Own libraries
Library         Keywordsinpython  
Library    DateTime
Library    String

*** Variables ***
${GLOBAL_RETRY_AMOUNT}=    4x
${GLOBAL_RETRY_INTERVAL}=    0.5s
${whitespace}    ${SPACE}
${underscore}    _

*** Keywords ***
#SEE .\KEYWORDSINPYTHON.PY

#Ask For The Orders Download Link
#    Add heading    Robocorp Certificate level II assignment. Input the download link for the orders.csv File.    size=Small
 #   Add text input   Inputlink    
 #   Add submit buttons    Continue
 #   ${downloadlink}=    Run Dialog 
 #   [Return]    ${downloadlink.Inputlink}

     


#Download The Orders File
#    [Arguments]    ${downloadlink}
#    Convert To String    ${downloadlink}
#    Download    ${downloadlink}   overwrite=True

#Open The RobotSpareBin Order Website
#    Open Available Browser    https://robotsparebinindustries.com/#/robot-order

#Close The Annoying Modal
#    Wait Until Element Is Visible    class:btn.btn-danger
#    Click Button   class:btn.btn-danger

#Fill The Order For One Person
#    [Arguments]    ${order}
#    ${modalvisible}=   Is Element Visible  class:btn.btn-danger    missing_ok=True
#    Run Keyword If   ${modalvisible}
#    ...    Close The Annoying Modal
#    ${head_as_string}=    Convert To String    ${order}[Head]
#    Select From List By Value    head    ${head_as_string}
#    Select Radio Button   body   ${order}[Body]
#    Input Text    class:form-control   ${order}[Legs]
#    Input Text    address   ${order}[Address]
#    Take Screenshot
#    Click Button    order
#    ${receiptvisible}=   Is Element Visible  receipt    missing_ok=True
#    Run Keyword Unless   ${receiptvisible}    
#    ...    Fill The Order For One Person    ${order}

    

#Take Screenshot
#   Wait Until Element Is Visible    preview    
#    Click Button    preview
#    Wait Until Element Is Visible    id:robot-preview-image    
#    Screenshot      id:robot-preview-image    ${CURDIR}${/}output${/}currentpicture.png

#Order Robots From RobotSpareBin Industries Inc
#    ${orders}=    Read table from CSV  orders.csv
#    FOR    ${order}    IN    @{orders}    
#        Fill The Order For One Person    ${order}
#        Save Receipt As PDF    ${order}
#        Wait Until Element Is Visible  id:order-another
#        Click Button  id:order-another
#    END

#Save Receipt As PDF
#    [Arguments]    ${order}
#    Wait Until Element Is Visible    receipt
#    ${order_receipt_html}=    Get Element Attribute    id:receipt    outerHTML
#    Html To Pdf    ${order_receipt_html}    ${CURDIR}${/}output${/}receipts${/}order_${order}[Order number]_receipt.pdf
#    Embed The Robot Screenshot To the Receipt PDF File    ${order}

    

#Embed The Robot Screenshot To the Receipt PDF File
 #   [Arguments]    ${order}  
 #  Open PDF    ${CURDIR}${/}output${/}receipts${/}order_${order}[Order number]_receipt.pdf
 #  Add Watermark Image To Pdf        
    #...    image_path=${CURDIR}${/}output${/}currentpicture.png
    #...    output_path=${CURDIR}${/}output${/}receipts${/}order_${order}[Order number]_receipt.pdf
    #Close PDF  ${CURDIR}${/}output${/}receipts${/}order_${order}[Order number]_receipt.pdf


    
End Log
    [Arguments]    ${logandreportdate}
    Log  Done.    
    Copy File    ${CURDIR}${/}log.html    ${CURDIR}${/}output${/}Logs and reports${/}log_${logandreportdate}.html
    Copy File    ${CURDIR}${/}report.html    ${CURDIR}${/}output${/}Logs and reports${/}report_${logandreportdate}.html          
    

*** Tasks ***
Insert The Order Data And Save Receipts As PDF With Embedded Screenshots And Zip
#Orders file: https://robotsparebinindustries.com/orders.csv
    ${credentials}=    Get Secret Credentials    
    ${url}=    Ask For Credentials And The Orders Download Link    ${credentials}
    #TODO: Convert To String missing implementation (Not needed?)
    Convert To String    ${url}
    Download The Orders File    ${url}
    Open The RobotSpareBin Order Website        
    Close The Annoying Modal 
    Order Robots From RobotSpareBin Industries Inc
    #TODO: Archive Folder With Zip missing Python implementation (Not needed?)
    Archive Folder With Zip    ${CURDIR}${/}output${/}receipts    ${CURDIR}${/}output${/}receipts.zip    
    #TODO: Close Browser missing implementation (Not needed?)
    Close Browser
    #TODO: End Log Missing Python implementation (Not needed?)
    Show Modal Click Attempts
    ${logandreportdate}=    Create Log And Report Timestamp
    [Teardown]    End Log    ${logandreportdate}
