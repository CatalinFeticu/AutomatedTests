import os
from telnetlib import EC
from turtle import home
from pages import homePage
from pages import searchPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class testCase(unittest.TestCase):
    def __init__(self,driver):
        self.driver = webdriver.Chrome(driver)
        self.driver.get("https://www.bayut.com/")
        self.HomePage = homePage.HomePage(self.driver)
        self.SearchPage = searchPage.searchPage(self.driver)


    @pytest.
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

        assert test == True


if __name__ == "__main__":
    a = testCase("chromedriver.exe")
    a.test_CheckLocationsOnAllPages("Al Faseel Area")
