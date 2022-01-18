import sys
sys.path.insert(0,'.//')
from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By


class searchPage():
    
    articles_xpath = "//li[@role='article']"
    article_location_xpath = "//div[@aria-label='Location']"
    next_button_xpath = "//div[@title='Next']"
    purpose_text_box_xpath = "//div[@aria-label='Purpose filter']/div/div/span/span"
    property_type_text_xpath = "//label[text()='property type']/following-sibling::div/span/span"
    location_text_xpath = "//span[@aria-label='Filter label']"

    def __init__(self,driver):
        self.driver = driver
        
    def getAllPropertyWebElements(self):
        return self.driver.find_elements("xpath",self.articles_xpath)
    
    def getLocationAllArticlesOnPage(self):
        textList = []
        for articles in self.driver.find_elements(By.XPATH,self.article_location_xpath):
            textList.append(articles.text)
        return textList

    def checkIfNextButtonExists(self):
        if len(self.driver.find_elements(By.XPATH,self.next_button_xpath)) != 0:
            return True
        return False
    
    def clickNextButton(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,self.SearchPage.next_button_xpath))


if __name__ == "__main__":

    test = searchPage(webdriver.Chrome("chromedriver.exe"))
    print(test.getLocationAllArticlesOnPage())

