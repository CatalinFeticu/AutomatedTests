import sys
sys.path.insert(0,r'./')
import pages.searchPage
import pages.homePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class LocationAllPages():
    def __init__(self,driverPath):
        self.driver = webdriver.Chrome(driverPath)
        self.HomePage = pages.homePage.HomePage(self.driver)
        self.SearchPage = pages.searchPage.searchPage(self.driver)


    def test_check_all_locations(self,LocationToSearch,checkAllPages = True):

        self.driver.get("https://www.bayut.com")

        
        test = True
        failedLocation = None
        pageArrow = True

        self.HomePage.inputLocation(LocationToSearch)
        self.HomePage.selectPurpose("Buy")
        self.HomePage.clickFind()

        while(pageArrow):
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(("xpath",self.SearchPage.article_location_xpath)))
            articles = self.SearchPage.getLocationAllArticlesOnPage()

            for x in articles:
                if LocationToSearch not in x:
                    failedLocation = x
                    test = False
                    break
            pageArrow = self.SearchPage.checkIfNextButtonExists()
            if pageArrow == True and checkAllPages == True:
                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.SearchPage.next_button_xpath))
            if checkAllPages == False:
                break
        self.driver.quit()
        return test

def test_locations_first_page():
    a = LocationAllPages("chromedriver.exe")
    assert a.test_check_all_locations("Dubai Marina",checkAllPages= False) == True


if __name__ == "__main__":
    a = LocationAllPages("chromedriver.exe")
    a.test_check_all_locations("Dubai Marina",checkAllPages= False)
    pass