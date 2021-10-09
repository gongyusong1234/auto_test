# coding=utf-8
import os,sys
from selenium.webdriver.support.wait import WebDriverWait
from config.read_ini import ReadIni

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,*args):
        data = ReadIni().read_my_ini(*args)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:

            if by == 'id':
                WebDriverWait(self.driver, 10, 0.1).until(lambda dv: self.driver.find_element_by_accessibility_id(value))
                return self.driver.find_element_by_accessibility_id(value)
            elif by == 'name':
                WebDriverWait(self.driver, 10, 0.1).until(lambda dv: self.driver.find_element_by_ios_predicate(f'{by}=={value}'))
                return self.driver.find_element_by_ios_predicate(f'{by}=={value}')
            elif by == 'type':
                WebDriverWait(self.driver, 10, 0.1).until(lambda dv: self.driver.find_element_by_ios_predicate(f'{by}=={value}'))
                return self.driver.find_element_by_ios_predicate(f'{by}=={value}')
            elif by == 'xpath':
                WebDriverWait(self.driver, 10, 0.1).until(lambda dv: self.driver.find_element_by_xpath(value))
                return self.driver.find_element_by_xpath(value)
            elif by == 'tap':
                return self.driver.tap([value])
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            print('\nby是=======>',by,'\nvalue是========>',value)
            self.driver.save_screenshot(os.path.join(os.path.join(os.path.dirname(os.getcwd()),'Image'),'%s.jpg'%value))
            return None


