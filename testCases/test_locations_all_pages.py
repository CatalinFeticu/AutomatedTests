import sys
sys.path.insert(0,'.//')
import pages.searchPage
import pages.homePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Test_LocationsAllPages:
    def __init__(self,driverPath):
        driverOptions = Options()
        driverOptions.add_argument('log-level=3')
        self.driver = webdriver.ChromeOptions(driverPath,driverOptions)
        self.HomePage = pages.homePage.HomePage(self.driver)
        self.SearchPage = pages.searchPage.searchPage(self.driver)

    def test_check_all_locations_on_all_pages(self,LocationToSearch):
        
        test = True
        failedLocation = None
        #homePage serach
        self.HomePage.inputLocation(LocationToSearch)
        self.HomePage.selectPurpose("Buy")
        self.HomePage.clickFind()

        pageArrow = True
        while(pageArrow):
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(("xpath",self.SearchPage.article_location_xpath)))
            #property check for location
            articles = self.SearchPage.getLocationAllArticlesOnPage()

            for x in articles:
                if LocationToSearch not in x:
                    failedLocation = x
                    test = False
                    break
            pageArrow = self.SearchPage.checkIfNextButtonExists()
            if pageArrow == True:
                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.SearchPage.next_button))

        return test == True

def test_hey():
    a = Test_LocationsAllPages("chromedriver.exe")
    assert a.test_check_all_locations_on_all_pages("Al Faseel Area") == True


if __name__ == "__main__":
    a = Test_LocationsAllPages("chromedriver.exe")
    a.test_check_all_locations_on_all_pages("Al Faseel Area")
    pass