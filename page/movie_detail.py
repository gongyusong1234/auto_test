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

    # 详情页点击片单
    def joincoollect(self):
        return self.find.get_element('MovieDetails', 'joincoollect')

    # 点击播放
    def play(self):
        return self.find.get_element('MovieDetails', 'play')






