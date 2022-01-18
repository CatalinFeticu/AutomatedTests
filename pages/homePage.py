from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class HomePage():
    
    location_input_textbox_xpath = "//ul[@aria-label='Location filter']/input"
    purpose_button_xpath = "//div[@aria-label='Purpose filter']/div/div"
    purpose_dropdown = dict()
    purpose_dropdown["Buy"] = "//button[@aria-label='Buy']"
    purpose_dropdown["Rent"] = "//button[@aria-label='Rent']"
    find_button_xpath = "//a[@aria-label='Find button']"
    popular_search_to_rent_button_xpath = "//div[text()='To Rent']"
    popular_search_to_for_sale_xpath = "//div[text()='For Sale']"
    popular_dubai_apartments_list_xpath_xpath = "//a[text()='Dubai Apartments']/parent::div/following-sibling::ul"
    view_all_apartments_rent_button_xpath = "//body/div[@id='body-wrapper']/main/div/div[@aria-label='Popular properties']/div[@class='_2fddc99a']/div[@class='b2688814']/div[@class='fc910dcd']/div/div[1]/div[2]"

    def __init__(self,driver):
        self.driver = driver
        driver.get("https://www.bayut.com")

    def inputLocation(self,location):
        a = listener()
        eventFire = EventFiringWebDriver(self.driver,a)
        eventFire.find_element(By.XPATH,self.location_input_textbox_xpath).click()
        eventFire.find_element(By.XPATH,self.location_input_textbox_xpath).send_keys(location)
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.location_input_textbox_xpath).send_keys(Keys.ENTER)

    def selectPurpose(self,option):

        self.driver.find_element(By.XPATH,self.purpose_button_xpath).click()
        self.driver.find_element(By.XPATH,self.purpose_dropdown[option]).click()
    
    def clickFind(self):
        self.driver.find_element(By.XPATH,self.find_button_xpath).click()

    def clickPopularSearchOption(self,option):
        if option == "Rent":
            self.driver.find_element(By.XPATH,self.popular_search_to_rent_button_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.popular_search_to_rent_button_xpath).click()      

    def getAllPopularLinkElementsOption(self,option):
        allPopularLinksList = self.driver.find_elements(By.XPATH,self.popular_dubai_apartments_list_xpath_xpath)
        if option == "Rent":
            return allPopularLinksList[1]
        else:
            return allPopularLinksList[0]

    def clickViewAllRent(self):
        self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH,self.view_all_apartments_rent_button_xpath))

class listener(AbstractEventListener):
    def on_exception(self):
        pass
    pass

if __name__ == "__main__":
    newTest = HomePage(webdriver.Chrome("chromedriver.exe"))

    newTest.inputLocation("Dubai Marina")
    newTest.selectPurpose("Buy")
    newTest.clickFind()