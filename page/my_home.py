# coding=utf-8

from base.basepage import FindElement

"""
个人页
"""


class My_Home:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 个人页我的片单
    def coollect_button(self):
        return self.find.get_element('MyMore', 'coollect')

    # 返回按钮
    def back(self):
        return self.find.get_element('MyMore', 'goback')


