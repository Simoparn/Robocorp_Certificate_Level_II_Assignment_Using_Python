
#Browser and UI libraries
import logging
from RPA.HTTP import HTTP
from RPA.Dialogs import Dialogs 
from RPA.Browser.Selenium import Selenium
#File and data handling libraries
from RPA.FileSystem import FileSystem
from RPA.PDF import DocumentKeywords
from RPA.Archive import Archive
from RPA.Excel.Files import Files
from RPA.Tables import Tables

#TODO: Logging library?
#from robot.output import logger
#Vault libraries
from RPA.Robocloud import Secrets

browser=Selenium()

#@Keyword definitions not needed with robot.yaml -> PYTHONPATH configured

class Keywordsinpython:
    

    def get_secret_credentials(self):
        secretmanager=Secrets.FileSecrets() 
        secrets=secretmanager.get_secret("credentials")
        getcredentials=[]
        getcredentials.append(secrets["username"])
        getcredentials.append(secrets["password"])
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
        
        orders=request.download(url, target_file="orders.csv", overwrite=True)
        filereader=Files()
        tablereader=Tables()
        #TODO: error, file format not supported or corrupted file
        ordersfile=filereader.open_workbook("./orders.csv")
        
        return ordersfile

 
    def open_the_robotSpareBin_order_website(self):
        url = "https://robotsparebinindustries.com/#/robot-order/"
        browser.open_available_browser(url)
        
    
    def close_the_annoying_modal(self):
        browser.click_element_when_visible("class:btn.btn-danger")
    
    
    def fill_the_order_for_one_person(self, order):
        selector=Selenium()
        
        modalvisible=browser.is_element_visible("class:btn.btn-danger")
        if  (modalvisible):
            self.close_the_annoying_modal() 
            head_as_string= order["head"]
            selector.select_from_list_by_value("head", head_as_string)
            selector.select_radio_button("body", order["body"])
            selector.input_text("class:form-control", order["Legs"])
            selector.input_text("address", order["Legs"])
            self.take_screenshot()
            selector.click_button("order")
            receiptvisible= browser.is_element_visible("receipt", missing_ok=True)
            #Can't access Builtin, run_keyword_unless()
            if(receiptvisible):
                self.fill_the_order_for_one_person(order)

    def take_screenshot(self):     
            selector=Selenium()
            selector.wait_until_element_is_visible("preview", timeout=5)
            selector.click_button("preview")
            selector.wait_until_element_is_visible("id:robot-preview-image", timeout=5)
            browser.screenshot("id:robot-preview-image", "./output/currentpicture.png")
                 
    
    
    def order_robots_from_robotsparebin_industries_inc(self, csv_orders):
        selector=Selenium() 
        #Not needed? filereader=Files()
        tablereader=Tables()
        
    
        #ordersastable = filereader.read_worksheet_as_table(csv_orders)
    
        orders=tablereader.read_table_from_csv("csv_orders", header=True)
        #ordersastable.filter_empty_rows(orders)
       
        
        for order in orders:
     
         if(order):  
            
        
            self.fill_the_order_for_one_person(order)
            self.save_receipt_as_PDF(order)
            selector.wait_until_element_is_visible("id:order-another")
            selector.click_button("id:order-another")
           
            
    
    
    def save_receipt_as_PDF(self, order):
        selector=Selenium()
        receiptfile=DocumentKeywords()
        selector.wait_until_element_is_visible("receipt")
        order_receipt_html = browser.get_element_attribute("id:receipt", "outerHTML") 
        receiptfile.html_to_pdf(order_receipt_html, "./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        #TODO: undefined
        self.embed_the_robot_screenshot_to_the_receipt_PDF_file(order)
        
    
    
    def embed_the_robot_screenshot_to_the_receipt_PDF_file(self, order):
        receiptfile=DocumentKeywords()
        receiptfile.open_pdf("./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        receiptfile.add_watermark_image_to_pdf(image_path="./output/currentpicture.png",output_path="./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        receiptfile.close_pdf("./output/receipts/order_"+order["Order number"]+"_receipt.pdf")

        
   



