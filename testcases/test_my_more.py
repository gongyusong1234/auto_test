import unittest
from appium import webdriver
from config.wddriver import desired_caps
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.video import Video


class Test_My_More(unittest.TestCase):
    """
    我的
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
        我的
        """
        print('首页进入个人页')
        self.home.my_home().click()

        print('我的页面点击关注')
        self.myhome.member().click()
        print('关注列表展现')
        # 拿到列表后判断列表是否为空
        self.myhome.mycheck_list

        print('关注列表第一位用户名：'+self.myhome.mycheck_list_firstname())

        print('点击返回 回到个人页')
        self.myhome.mycheck_back().click()

        print('我的页面点击粉丝')
        self.myhome.filmreview().click()
        self.myhome.fans().click()

        print('粉丝页第一位用户名：'+self.myhome.my_fans_list_firstname())

        print('粉丝页点击返回 回到个人页')
        self.myhome.my_fans_back().click()

        print('我的页面点击影评')
        self.myhome.filmreview().click()

        print('影评总数：'+self.myhome.finmreview_total())
        # 如果影评为空时 不去走下面的获取影评信息，而是去添加影评
        print('第一位影评：'+self.myhome.finmreview_firsttext())

        print('影评页返回个人页')
        self.myhome.finmreview_back().click()
