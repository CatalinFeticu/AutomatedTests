from cgitb import text
from selenium import webdriver

class searchPage():
    articles_xpath = "//li[@role='article']"
    article_location_xpath = "//div[@aria-label='Location']"
    next_button = "//div[@title='Next']"

    def __init__(self,driver):
        self.driver = driver

    def getAllPropertyWebElements(self):
        return self.driver.find_elements("xpath",self.articles_xpath)
    
    def getLocationAllArticlesOnPage(self):
        textList = []
        for articles in self.driver.find_elements_by_xpath(self.article_location_xpath):
            textList.append(articles.text)
        return textList

    def checkIfNextButtonExists(self):
        if len(self.driver.find_elements_by_xpath(self.next_button)) != 0:
            return True
        return False

if __name__ == "__main__":

    test = searchPage(webdriver.Chrome("chromedriver.exe"))
    print(test.getLocationAllArticlesOnPage())

