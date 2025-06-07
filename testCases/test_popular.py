import sys
sys.path.insert(0,".//")
import pages.searchPage
import pages.homePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time

class PopularClassForTest():
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

    def test_all_links_popular_tab(self,option = "Rent"):
        
        self.driver.get("https://www.bayut.com")

        test = True
        failedLink = []

        self.HomePage.clickPopularSearchOption("Rent")
        self.HomePage.clickViewAllRent()

        popularLinks = self.HomePage.getAllPopularLinkElementsOption("Rent")
        listLinks = popularLinks.find_elements(By.XPATH,".//li//a")

        for link in listLinks:
            textCheck = "".join([txt for txt in link.text if txt.isalnum()])
            href = link.get_attribute("href")

            self.driver.execute_script(f"window.open('{href}');")
            self.driver.switch_to.window(self.driver.window_handles[1])

            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(("xpath",self.SearchPage.location_text_xpath)))

            optionCheck = self.driver.find_element(By.XPATH,self.SearchPage.purpose_text_box_xpath).text
            typeCheck = self.driver.find_element(By.XPATH,self.SearchPage.property_type_text_xpath).text
            filterText = "".join([e for e in self.driver.find_element(By.XPATH,self.SearchPage.location_text_xpath).text if e.isalnum()])


            if optionCheck != option:
                test = False
                failedLink.append((optionCheck,option))

            if textCheck not in filterText:
                test = False
                failedLink.append((filterText,textCheck))

            if typeCheck != "Apartment":
                test= False
                failedLink.append((typeCheck,"Apartment"))

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
1.0-SNAPSHO1.0-SNAPSHOTsodijfoiasjdfoijTef test_popular_apartments_links():
    a = PopularClassForTest("Chrome")
    test = a.test_all_links_popular_tab()
    assert test[0] == True and test[1] == []

if __name__ == "__main__":
    a = PopularClassForTest("Chrome")
    print(a.test_all_links_popular_tab())
    