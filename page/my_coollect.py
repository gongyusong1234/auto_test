# coding=utf-8

from base.basepage import FindElement

"""
我的片单页
"""
class My_Coollect:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 片单页 第一位的名称
    def first_move_name(self):
        return self.find.get_element('My_Coollect', 'first_move_name').text

    # 片单页 第一位的相关信息
    def first_move_other(self):
        return self.find.get_element('My_Coollect', 'first_move_other').text


