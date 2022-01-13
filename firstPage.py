from selenium import webdriver 
import time

class baseCode():
    location_input_textbox_xpath = "//ul[@aria-label='Location filter']/input"
    purpose_button_xpath = "//div[@aria-label='Purpose filter']/div/div"
    purpose_dropdown = dict()
    purpose_dropdown["Buy"] = "//button[@aria-label='Buy']"
    purpose_dropdown["Rent"] = "//button[@aria-label='Rent']"
    # purpose_dropdown_select_buy_xpath = "//button[@aria-label='Buy']"
    # purpose_dropdown_select_rent_xpath = "//button[@aria-label='Rent']"
    find_button_xpath = "//a[@aria-label='Find button']"


    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        
        self.driver.get("https://bayut.com/")

    def inputLocation(self,location):
        

        # self.driver.get("https://www.bayut.com/")

        self.driver.find_element_by_xpath(self.location_input_textbox_xpath).send_keys(location)

    def selectPurpose(self,option):

        self.driver.find_element_by_xpath(self.purpose_button_xpath).click()
        self.driver.find_element_by_xpath(self.purpose_dropdown[option]).click()

    
    def clickFind(self):
        self.driver.find_element_by_xpath(self.find_button_xpath).click()
        time.sleep(3)

testcase = baseCode()

testcase.inputLocation("Dubai")
testcase.selectPurpose("Buy")
testcase.clickFind()

