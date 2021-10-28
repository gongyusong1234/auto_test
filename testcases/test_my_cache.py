import unittest
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.video import Video


class Test_My_Cache(unittest.TestCase):
    """
    我的缓存
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.videohall = My_Movie(ios_driver)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.play = Video(ios_driver)

    def test_1(self):
        """
        我的缓存
        """
        print('搜索内容 进入详情页')
        print('点击下载进行缓存')
        print('清晰度 选择选择标清再选择高清')
        print('进行缓存')

        print('回到首页')
        print('进入个人中心 点击我的缓存')
        print('查看我的缓存第一位 与添加到缓存的电影一致')
        print('点击缓存电影 进入播放器')
        print('暂停 / 开始 / 标题 / 进度条 / 清晰度 / 全屏控件展示正常')

        print('返回个人页，返回首页 点击搜索')
        print('搜索内容 进入详情页')
        print('点击下载进行缓存，校验提示无法缓存')
        print('返回搜索，搜索其他内容，进入详情页')
        print('点击下载进行缓存')

















