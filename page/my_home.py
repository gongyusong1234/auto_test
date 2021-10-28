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

    # 关注列表
    def member(self):
        return self.find.get_element('MyMore', 'attention')

    def mycheck_back(self):
        return self.find.get_element('Mycheck', 'mycheck_back')

    def mycheck_list(self):
        return self.find.get_element('Mycheck', 'mycheck_list')

    def mycheck_list_firstname(self):
        return self.find.get_element('Mycheck', 'mycheck_list_firstname').text

    def mycheck_first_cancel(self):
        return self.find.get_element('Mycheck', 'mycheck_first_cancel')

    # 粉丝列表
    def fans(self):
        return self.find.get_element('MyMore', 'fans')

    def my_fans_back(self):
        return self.find.get_element('My_Fans', 'my_fans_back')

    def my_fans_list_firstname(self):
        return self.find.get_element('My_Fans', 'my_fans_list_firstname').text

    # 影评列表
    def filmreview(self):
        return self.find.get_element('MyMore', 'filmreview')

    def finmreview_back(self):
        return self.find.get_element('Filmreview', 'finmreview_back')

    def finmreview_total(self):
        return self.find.get_element('Filmreview', 'finmreview_total').text

    def finmreview_firsttext(self):
        return self.find.get_element('Filmreview', 'finmreview_firsttext').text



    # 我的设置




