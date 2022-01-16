import sys
sys.path.insert(0,".//")
import pages.searchPage
import pages.homePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

class PopularClassForTest():
    def __init__(self,driverPath):
        self.driver = webdriver.Chrome(driverPath)
        self.HomePage = pages.homePage.HomePage(self.driver)
        self.SearchPage = pages.searchPage.searchPage(self.driver)
        self.driver.get("https://www.bayut.com")

    def test_all_links_popular_tab(self,option = "Rent"):
        
        test = True
        failedLink = []
        
        self.HomePage.clickPopularSearchOption("Rent")
        self.driver.execute_script("arguments[0].click();",self.driver.find_element_by_xpath(self.HomePage.view_all_apartments_rent_button_xpath))

        popularLinks = self.HomePage.getAllPopularLinkElementsOption(option)
        listLinks = popularLinks.find_elements_by_xpath(".//li//a")
        for link in listLinks:
            textCheck = "".join([e for e in link.text if e.isalnum()])
            href = link.get_attribute("href")
            print(href)
            self.driver.execute_script(f"window.open('{href}');")
            self.driver.switch_to.window(self.driver.window_handles[1])

            filterText = "".join([e for e in self.driver.find_element_by_xpath(self.SearchPage.location_text_xpath).text if e.isalnum()])

            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(("xpath",self.SearchPage.location_text_xpath)))

            if self.driver.find_element_by_xpath(self.SearchPage.purpose_text_box_xpath).text != option:
                test = False
                failedLink.append(textCheck)

            if textCheck not in filterText:
                test = False
                failedLink.append((filterText,textCheck))

            if self.driver.find_element_by_xpath(self.SearchPage.property_type_text_xpath).text != "Apartment":
                test= False
                failedLink.append(textCheck)

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.quit()
        return test,failedLink



def test_popular_apartments_links():
    a = PopularClassForTest("chromedriver.exe")
    test = a.test_all_links_popular_tab()
    assert test[0] == True and test[1] == []

        # self.driver.quit()

if __name__ == "__main__":
    a = PopularClassForTest("chromedriver.exe")
    print(a.test_all_links_popular_tab())
    