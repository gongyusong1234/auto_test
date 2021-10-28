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

    # 一拳超人详情页概要
    def yqcrtitle_button(self):
        return self.adc.get_element('MovieDetails', 'yqcrdetail')

    # 白鹿原详情页概要
    def blytitle_button(self):
        return self.adc.get_element('MovieDetails', 'blydetail')

    # 斯巴达克斯详情页概要
    def sbdkstitle_button(self):
        return self.adc.get_element('MovieDetails', 'sbdksdetail')

    # 详情页 x 键
    def close_button(self):
        return self.adc.get_element('MovieDetails', 'close')






