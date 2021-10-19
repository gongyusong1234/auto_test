# coding=utf-8

from base.basepage import FindElement

"""
 影片详情页
"""
class Movie_Detail:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 详情页返回
    def detail_close(self):
        return self.find.get_element('MovieDetails', 'close')




