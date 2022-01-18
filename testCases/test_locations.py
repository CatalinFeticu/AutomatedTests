import sys
sys.path.insert(0,r'./')
import pages.searchPage
import pages.homePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


class LocationAllPages():
    def __init__(self,driverName):
        if driverName == "Chrome":
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.chrome.options import Options
            option =  Options()
            option.add_argument("--log-level=3")
            chromeService = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chromeService,options=option)
        if driverName == "FireFox":
            from selenium.webdriver.firefox.service import Service
            from selenium.webdriver.firefox.options import Options
            option =  Options()
            option.add_argument("--log-level=3")
            firefoxService = Service(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service = firefoxService,options = option)

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
                self.SearchPage.clickNextButton()

            if checkAllPages == False:
                break

        self.driver.quit()
        return test

def test_locations_first_page():
    a = LocationAllPages("Chrome")
    assert a.test_check_all_locations("Dubai Marina",checkAllPages= False) == True


if __name__ == "__main__":
    a = LocationAllPages("Chrome")
    a.test_check_all_locations("Dubai Marina",checkAllPages= False)
    pass