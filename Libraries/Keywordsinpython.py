
#Browser and UI libraries
from RPA.HTTP import HTTP
from RPA.Dialogs import Dialogs 
from RPA.Browser.Selenium import Selenium
from RPA.PDF.keywords.document import DocumentKeywords, LibraryContext
#from selenium import webdriver -> Can't use without setting system variable PATH
#File and data handling libraries
from RPA.FileSystem import FileSystem
from RPA.PDF import PDF
from RPA.Archive import Archive
from RPA.Excel.Files import Files
from RPA.Tables import Tables
#import csv
#TODO: Logging library?
#from robot.output import logger
#from robot.libraries.BuiltIn import logger
#Vault libraries
from RPA.Robocorp import Secrets

global_timeout=3

browser=Selenium()
pdf=PDF()
#webdriverchrome=webdriver.Chrome()

#@Keyword definitions not needed with robot.yaml -> PYTHONPATH configured

class Keywordsinpython:


    def get_secret_credentials(self):
        secretmanager=Secrets.FileSecrets() 
        vault=secretmanager.get_secret("username_and_password")
        getcredentials=[]
        getcredentials.append(vault["username"])
        getcredentials.append(vault["password"])
        return getcredentials

    
    def ask_for_credentials_and_the_orders_download_link(self, credentials):
        dialog=Dialogs()
        rightcredentials=False
        while not(rightcredentials):
            #Add heading  (self, heading: str, size: Size = Size.Medium,)
            dialog.add_heading("Robocorp Certificate II using Python, Simo P.")    
            #Add input      (self, name: str, label: Optional[str] = None, placeholder: Optional[str] = None, rows: Optional[int] = None,)
            dialog.add_text_input("Username", "Enter username")
            dialog.add_text_input("Password", "Enter password")
            dialog.add_text_input("Url", "Enter the orders URL here")
            #Add submit buttons
            dialog.add_submit_buttons("Press here to download the orders file")
            #Run the dialog (self, timeout: int = 180, **options: Any)
            inputlinkdialog= dialog.run_dialog()
            if not(inputlinkdialog["Username"] == credentials[0] and inputlinkdialog["Password"] == credentials[1]):
                rightcredentials=False
                dialog.add_text("Wrong username or password, try again.")
            else:
                rightcredentials=True
        return inputlinkdialog["Url"]


    def download_the_orders_file(self, url):    
        
        request=HTTP()
        filemanager=FileSystem()
        #Use for personal testing if file already loaded and requests exceeded:
        file=filemanager.read_file("./orders.csv","utf-8")
        if not (file):
            ordersfile=request.download(url, target_file="orders.csv", overwrite=True)
        

 
    def open_the_robotSpareBin_order_website(self):
        url = "https://robotsparebinindustries.com/#/robot-order/"
        browser.open_available_browser(url)
        
       
    
    def close_the_annoying_modal(self):
        try:
            browser.wait_until_element_is_visible("class:btn.btn-danger", timeout=1)
            browser.click_button("class:btn.btn-danger")
        except:
            pass
    
    
    def fill_the_order_for_one_person(self, order):

        #IF/ELSE-structure is recommended by Robot Framework documentation (see robot.libraries.BuiltIn) instead of run_keyword_if()
        #This is needed with Python for the page to load properly before checking for the modal
        #TODO: use is_displayed() instead?
        
        #modalbutton=webdriverchrome.find_element_by_class_name("class:btn.btn-danger")
        #if(modalbutton.is_displayed()):
        #    self.close_the_annoying_modal()
        
        #if(browser.is_element_visible("class:btn.btn-danger", missing_ok=True)):
        self.close_the_annoying_modal() 
        #else:
        head_as_string= order["Head"]
        browser.select_from_list_by_value("head", head_as_string)
        browser.select_radio_button("body", order["Body"])
        browser.input_text("class:form-control", order["Legs"])
        browser.input_text("address", order["Legs"])
        self.take_screenshot()
        
        while not(browser.is_element_visible("receipt", missing_ok=True)):
            browser.click_button("order")
        
    

        #Replaced unnecessary recursion, order can be sent by repeatedly pressing the button without refilling
        # try:
        #    browser.wait_until_element_is_visible("id:receipt", global_timeout)
        #except:
        #    if not(browser.is_element_visible("id:receipt", missing_ok=True)):
        #     self.fill_the_order_for_one_person(order)
        
    
    def take_screenshot(self):  
           
        browser.wait_until_element_is_visible("preview", global_timeout)
        browser.click_button("preview")
        browser.wait_until_element_is_visible("id:robot-preview-image", global_timeout)
        browser.screenshot("id:robot-preview-image", "./Output/currentpicture.png")
                 
    
    
    
    def order_robots_from_robotsparebin_industries_inc(self):
        
        
        tablereader=Tables()
        
        orders=tablereader.read_table_from_csv(".\orders.csv", header=True)
        tablereader.filter_empty_rows(orders)

        #Alternatively:
        #with open('orders.csv') as csvFile:
            #list of dictionaries, https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
            #orders = [{k: v for k, v in row.items()} for row in csv.DictReader(ordersfile, skipinitialspace=True)]
        
        for order in orders:
         if(order):            
            self.fill_the_order_for_one_person(order) 
            #try:
            self.save_receipt_as_PDF(order)
            #except TypeError:
            #    logger.console(ErrorDetails)
            browser.wait_until_element_is_visible("id:order-another", global_timeout)
            browser.click_button("id:order-another")
             
    
    def save_receipt_as_PDF(self, order):
            pdf=PDF()
            browser.wait_until_element_is_visible("id:receipt", timeout=global_timeout)
            order_receipt_html = browser.get_element_attribute("id:receipt", "outerHTML") 
            pdf.html_to_pdf(order_receipt_html, "./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
            self.embed_the_robot_screenshot_to_the_receipt_PDF_file(order)
       
    
    def embed_the_robot_screenshot_to_the_receipt_PDF_file(self, order):
        
        receiptfilewithimage=PDF()
        receiptfilewithimage.open_pdf("./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        receiptfilewithimage.add_watermark_image_to_pdf(image_path="./output/currentpicture.png",output_path="./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        receiptfilewithimage.close_pdf("./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
      
              
   #TODO: implementation for Archive Folders With Zip missing. (Unnecessary?)



