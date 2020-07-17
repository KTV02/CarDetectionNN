from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,pw):
        cookie="/html/body/div/div[1]/div[2]/div[2]/div"
       
        self.driver=webdriver.Firefox()
        self.driver.get("https://cookieclicker.io/")
        sleep(2)

        while(True):
            for i in range(100):
                self.driver.find_element_by_xpath(cookie).click()
            #check for time Machine upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[8]").click()
            #check portal upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[7]").click()
            #check for alchemy lab upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[6]").click()
            #check for shimpment upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[5]").click()
            #check for Mine upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[4]").click()
            #check for factory upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[3]").click()
            #check for grandma upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]").click()
            #check for cursor upgrade
            self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]").click()


       
    

InstaBot("natan_ul","QhVqyFf34VhNyQpJ4TRG")
