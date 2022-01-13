import os
from telnetlib import EC
from turtle import home
from pages import homePage
from pages import searchPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class testCase:
    def __init__(self,driver):
        self.driver = webdriver.Chrome(driver)
        self.driver.get("https://www.bayut.com/")
        self.HomePage = homePage.HomePage(self.driver)
        self.SearchPage = searchPage.searchPage(self.driver)

    def checkLocationsOnPage(self,LocationToSearch):
        
        test = True

        #homePage serach
        self.HomePage.inputLocation(LocationToSearch)
        self.HomePage.selectPurpose("Buy")
        self.HomePage.clickFind()

        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(("xpath",self.SearchPage.article_location_xpath)))
        #property check for location
        articles = self.SearchPage.getLocationAllArticlesOnPage()

        for x in articles:
            if LocationToSearch not in x:
                print(x)
                test = False
                break
        assert test == True

if __name__ == "__main__":
    a = testCase("chromedriver.exe")
    a.checkLocationsOnPage("Dubai Marina")
    
