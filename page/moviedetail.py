from base.basepage import FindElement
class MovieDetails:
    """影片详情页面"""
    def __init__(self,driver):
        self.driver = driver
        self.adc = FindElement(driver)

    #一拳超人详情页概要
    def yqcrtitle_button(self):
        return self.adc.get_element('MovieDetails','yqcrdetail')
    #白鹿原详情页概要
    def blytitle_button(self):
        return self.adc.get_element('MovieDetails','blydetail')
    #斯巴达克斯详情页概要
    def sbdkstitle_button(self):
        return self.adc.get_element('MovieDetails','sbdksdetail')
    #详情页 x 键
    def close_button(self):
        return self.adc.get_element('MovieDetails','close')
