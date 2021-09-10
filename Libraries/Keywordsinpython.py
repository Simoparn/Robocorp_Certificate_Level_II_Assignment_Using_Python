
#Browser and UI libraries
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
#from Robocloud import Secrets
#from RPA.Secrets import Vault

browser=Selenium()

#@Keyword definitions should not be needed with robot.yaml -> PYTHONPATH?

class Keywordsinpython:
    
    def ask_for_the_orders_download_link(self):
        dialog=Dialogs()
        #Add heading  (self, heading: str, size: Size = Size.Medium,)
        dialog.add_heading("Robocorp Certificate II using Python, Simo P.")    
        #Add input      (self, name: str, label: Optional[str] = None, placeholder: Optional[str] = None, rows: Optional[int] = None,)
        dialog.add_text_input("Url")
        #Add submit buttons
        dialog.add_submit_buttons("Press here to download the orders file")
        #Run the dialog (self, timeout: int = 180, **options: Any)
        inputlink= dialog.run_dialog()
        return inputlink["Url"]

    #@keyword("Download The Orders File")
    def download_the_orders_file(self, url):    
        
        request=HTTP()
        
        orders=request.download(url, target_file="orders.csv", overwrite=True)
        filereader=Files()
        tablereader=Tables()
        #TODO: error, file format not supported or corrupted file
        ordersfile=filereader.open_workbook("./orders.csv")
        
        return ordersfile

    #@keyword("Open The RobotSpareBin Order Website")
    def open_the_robotSpareBin_order_website(self):
        url = "https://robotsparebinindustries.com/#/robot-order/"
        browser.open_available_browser(url)
        
    #@keyword("Close The Annoying Modal")
    def close_the_annoying_modal(self):
        browser.click_element_when_visible("class:btn.btn-danger")
    
    #@keyword("Fill The Order For One Person")
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
                 
    
    #@keyword("Order Robots From RobotSpareBin Industries Inc")
    def order_robots_from_robotsparebin_industries_inc(self, csv_orders):
        selector=Selenium() 
        #Not needed? filereader=Files()
        tablereader=Tables()
        
    
        #ordersastable = filereader.read_worksheet_as_table(csv_orders)
    
        orders=tablereader.read_table_from_csv("csv_orders", header=True)
        #ordersastable.filter_empty_rows(orders)
       
        
        for order in orders:
     
         if(order):  
            #TODO: NOT NEEDED
            #order = {
            #    "ordernumber": order["Order number"],
            #    "head": int(order["Head"]),
            #    "body": int(order["Body"]),
            #    "legs": int(order["Legs"]),
            #    "address": order["Address"]
            #}
            self.fill_the_order_for_one_person(order)
            self.save_receipt_as_PDF(order)
            selector.wait_until_element_is_visible("id:order-another")
            selector.click_button("id:order-another")
           
            
    
    #@keyword("Save Receipt As PDF")
    def save_receipt_as_PDF(self, order):
        selector=Selenium()
        receiptfile=DocumentKeywords()
        selector.wait_until_element_is_visible("receipt")
        order_receipt_html = browser.get_element_attribute("id:receipt", "outerHTML") 
        receiptfile.html_to_pdf(order_receipt_html, "./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        #TODO: undefined
        self.embed_the_robot_screenshot_to_the_receipt_PDF_file(order)
        
    
    #@keyword("Embed The Robot Screenshot To The Receipt PDF File")
    def embed_the_robot_screenshot_to_the_receipt_PDF_file(self, order):
        receiptfile=DocumentKeywords()
        receiptfile.open_pdf("./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        receiptfile.add_watermark_image_to_pdf(image_path="./output/currentpicture.png",output_path="./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        receiptfile.close_pdf("./output/receipts/order_"+order["Order number"]+"_receipt.pdf")
        
   
    #@keyword("End Log")
    #TODO: Lacks working implementation
    #def end_log(self):
    #    return



