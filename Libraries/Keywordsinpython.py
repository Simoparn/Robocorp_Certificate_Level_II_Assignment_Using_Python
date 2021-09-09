
#Browser and UI libraries
from RPA.HTTP import HTTP
from RPA.Dialogs import Dialogs 
from RPA.Browser.Selenium import Selenium
#File handling libraries
from RPA.FileSystem import FileSystem
from RPA.PDF import PDF
from RPA.Archive import Archive
from RPA.Excel.Files import Files
from RPA.Tables import Tables
#Selector libraries
import SeleniumLibrary
#Vault libraries
#from Robocloud import Secrets
#from RPA.Secrets import Vault

browser=Selenium()
#@Keyword definitions should not be needed with robot.yaml -> PYTHONPATH?

class Keywordsinpython:
    
    def ask_for_the_orders_download_link(self):
        dialog=Dialogs()
        #Add heading  (self, heading: str, size: Size = Size.Medium,)
        dialog.add_heading("Robocop Certificate II using Python, Simo P.")    
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
        orders=request.download(url, overwrite=True)
        return orders

    #@keyword("Open The RobotSpareBin Order Website")
    def open_the_robotSpareBin_order_website(self):
        url = "https://robotsparebinindustries.com/#/robot-order/"
        browser.open_available_browser(url)
        
    #@keyword("Close The Annoying Modal")
    def close_the_annoying_modal(self):
        browser.click_element_when_visible("class:btn.btn-danger")
    #TODO: TÄSSÄ MENNÄÄN
    #@keyword("Fill The Order For One Person")
    def fill_the_order_for_one_person(self, order):
        selector=SeleniumLibrary()
        modalvisible=browser.is_element_visible("class:btn.btn-danger")
        if  (modalvisible):
            self.close_the_annoying_modal() 
            head_as_string= order["head"]
            selector.select_from_list_by_value()
            
                 
    
    #@keyword("Order Robots From RobotSpareBin Industries Inc")
    def order_robots_from_robotsparebin_industries_inc(self, csv_orders):
        

        #TODO: Files() not needed?
        #ordersfile=Files()
        #ordersastable = ordersfile.read_worksheet_as_table(csv_orders)
        
        ordersastable=Tables()
        orders=ordersastable.read_table_from_csv(csv_orders, header=True)
        ordersastable.filter_empty_rows(orders)
       
        
        for order in ordersastable:
           
            order = {
                "ordernumber": order["Order number"],
                "head": int(order["Head"]),
                "body": int(order["Body"]),
                "legs": int(order["Legs"]),
                "address": order["Address"]
            }
            self.fill_the_order_for_one_person(order)

        
    
    #@keyword("Save Receipt As PDF")
    def save_receipt_as_PDF():
        return
    
    #@keyword("Embed The Robot Screenshot To The Receipt PDF File")
    def embed_the_robot_screenshot_to_the_receipt_PDF_file(self):
        return
   
    #@keyword("End Log")
    def end_log(self):
        return



