from base.basepage import FindElement
class HomePage:
    """
    首页
    """
    def __init__(self,driver):
        self.driver = driver
        self.adc = FindElement(driver)

    # 底导首页按钮
    def firstpage_button(self):
        return self.adc.get_element('HomePage', 'firstpage')

    # 底导搜索按钮
    def seek_button(self):
        return self.adc.get_element('HomePage', 'seek')
    #底导 即将上下
    def becoming_button(self):
        return self.adc.get_element('HomePage', 'becoming')
    #底导放映厅
    def videohall_button(self):
        return self.adc.get_element('HomePage', 'videohall')
    #剧集
    def episode_button(self):
        return self.adc.get_element('HomePage', 'episode')
    #电影
    def movie_button(self):
        return self.adc.get_element('HomePage', 'movie')
    #类别
    def classes_button(self):
        return self.adc.get_element('HomePage', 'classes')
    #每日推荐 片单
    def moviecollect_button(self):
        return self.adc.get_element('HomePage', 'moviecollect')
    #每日推荐 播放
    def play_button(self):
        return self.adc.get_element('HomePage', 'play')
    #每日推荐 详情
    def details_button(self):
        return self.adc.get_element('HomePage', 'details')
    #精彩导视 第二个小视频
    def wonderfulrecommend_button(self):
        return self.adc.get_element('HomePage', 'wonderfulrecommend')
    #继续观看 栏目名称
    def golooktitle_button(self):
        return self.adc.get_element('HomePage', 'golooktitle')

    # 继续观看 >
    def golook_button(self):
        return self.adc.get_element('HomePage', 'golook')

    # 我的片单 栏目名称
    def mymoviecollecttitle_button(self):
        return self.adc.get_element('HomePage', 'mymoviecollecttitle')

    # 我的片单 >
    def mymoviecollect_button(self):
        return self.adc.get_element('HomePage', 'mymoviecollect')