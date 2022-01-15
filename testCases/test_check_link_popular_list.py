import sys
sys.path.insert(0,'.//')
import pages.searchPage
import pages.homePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class testClass():
    def __init__(self,driverPath):
        self.driver = webdriver.Chrome(driverPath)
        self.HomePage = pages.homePage.HomePage(self.driver)
        self.SearchPage = pages.searchPage.searchPage(self.driver)
        self.driver.get("https://www.bayut.com")

    def test_all_links_popular_tab(self,option = "Rent"):

        popularLinks = self.HomePage.getAllPopularLinkElementsOption(option)
        for link in popularLinks:
            link.click()

if __name__ == "main":
    a = testClass("chromedriver.exe")
    a.test_all_links_popular_tab()
    pass