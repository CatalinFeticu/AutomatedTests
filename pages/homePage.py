from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class HomePage():
    location_input_textbox_xpath = "//ul[@aria-label='Location filter']/input"
    purpose_button_xpath = "//div[@aria-label='Purpose filter']/div/div"
    purpose_dropdown = dict()
    purpose_dropdown["Buy"] = "//button[@aria-label='Buy']"
    purpose_dropdown["Rent"] = "//button[@aria-label='Rent']"
    # purpose_dropdown_select_buy_xpath = "//button[@aria-label='Buy']"
    # purpose_dropdown_select_rent_xpath = "//button[@aria-label='Rent']"
    find_button_xpath = "//a[@aria-label='Find button']"


    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://www.bayut.com")
    def inputLocation(self,location):
        


        self.driver.find_element_by_xpath(self.location_input_textbox_xpath).send_keys(location)
        self.driver.implicitly_wait(.5)

        self.driver.find_element_by_xpath(self.location_input_textbox_xpath).send_keys(Keys.ENTER)




        #For selectPurpose option should either be "Buy" or "Rent"
    def selectPurpose(self,option):

        self.driver.find_element_by_xpath(self.purpose_button_xpath).click()
        self.driver.find_element_by_xpath(self.purpose_dropdown[option]).click()


    
    def clickFind(self):
        self.driver.find_element_by_xpath(self.find_button_xpath).click()
        time.sleep(3)

if __name__ == "__main__":
    newTest = HomePage(webdriver.Chrome("chromedriver.exe"))

    newTest.inputLocation("Dubai Marina")
    newTest.selectPurpose("Buy")
    newTest.clickFind()