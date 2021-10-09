#coding=utf-8

from base.basepage import FindElement
class Dmo:
    def __init__(self,driver):
        self.driver = driver
        self.adc = FindElement(driver)

    #登录注册按钮
    def newlogin_button(self):
        return self.adc.get_element('LoginElement','newlogin')

    # 登录页手机号文本框
    def phonenum_button(self):
        return self.adc.get_element('LoginElement', 'phonenum')

    # 登录页获取验证码按钮
    def yanzhengma_button(self):
        return self.adc.get_element('LoginElement', 'yanzhengma')
    #输入按钮
    def shuru_button(self):
        return self.adc.get_element('LoginElement','shuru')
    def qingchu_button(self):
        return self.adc.get_element('LoginElement','qingchu')


