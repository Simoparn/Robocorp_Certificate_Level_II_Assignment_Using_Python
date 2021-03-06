
#Browser and UI libraries
from logging import log
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
from robot.libraries import DateTime
from robot.libraries import String
#Logging libraries
#from robot.output import logger
#from robot.libraries.BuiltIn import logger
#Vault libraries
#RPA.robocorp Vault not available in VS Code extension?
from RPA.Robocloud import Secrets

global_timeout=3


browser=Selenium()
pdf=PDF()
#webdriverchrome=webdriver.Chrome()

#@Keyword definitions not needed with robot.yaml -> PYTHONPATH configured

class Keywordsinpython:

    modal_click_attempts=0

    def get_secret_credentials(self):
        #When deploying locally: secretmanager= Secrets.FileSecrets(secret_file="vault.json")
        secretmanager=Secrets.RobocloudVault() 
        vault=secretmanager.get_secret("Cert_II_Credentials")
        getcredentials=[]
        getcredentials.append(vault["username"])
        getcredentials.append(vault["password"])
        return getcredentials

    
    def ask_for_credentials_and_the_orders_download_link(self, credentials):
        dialog=Dialogs()
        rightcredentials=False
        while not(rightcredentials):
            #Add heading  (self, heading: str, size: Size = Size.Medium,)
            dialog.add_heading("Robocorp Certificate II using Python, Simo P. (https://robotsparebinindustries.com/#/)")    
            #Add input      (self, name: str, label: Optional[str] = None, placeholder: Optional[str] = None, rows: Optional[int] = None,)
            dialog.add_text_input("Username", "Enter username")
            dialog.add_text_input("Password", "Enter password")
            dialog.add_text_input("Url", "Enter the orders URL here (https://robotsparebinindustries.com/orders.csv)")
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
        try:
            file=filemanager.read_file("./orders.csv","utf-8")
        except FileNotFoundError:
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
        
        #use is_displayed() instead, when importing selenium.webdriver
        #modalbutton=webdriverchrome.find_element_by_class_name("class:btn.btn-danger")
        #if(modalbutton.is_displayed()):
        #    self.close_the_annoying_modal()
        
        self.close_the_annoying_modal() 

        head_as_string= order["Head"]
        browser.select_from_list_by_value("head", head_as_string)
        browser.select_radio_button("body", order["Body"])
        browser.input_text("class:form-control", order["Legs"])
        browser.input_text("address", order["Legs"])
        self.take_screenshot()
        
        while not(browser.is_element_visible("receipt", missing_ok=True)):
            browser.click_button("order")
            self.modal_click_attempts+=1
            
            
        
    

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
            self.save_receipt_as_PDF(order)
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
      

    def show_modal_click_attempts(self):
        dialog=Dialogs()
        self.modal_click_attempts
        dialog.add_heading("Receipts saved. "+str(self.modal_click_attempts)+" modal click attempts in total.") 
        dialog.add_submit_buttons("Press here to end the program.")
        dialog.run_dialog()    

    def create_log_and_report_timestamp(self):
        logandreportdate=DateTime.get_current_date(result_format="%Y-%m-%d-%H-%M-%S")
        logandreportdate=logandreportdate.replace(" ","_")
        return logandreportdate

   #TODO: implementation for Archive Folders With Zip missing. (Unnecessary?)


 



