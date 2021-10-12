import unittest
import time
from appium import webdriver
import sys
from config.wddriver import desired_caps
from page.seek import Seek
from page.fristhome import HomePage
from page.moviedetail import MovieDetails


class TestSeek(unittest.TestCase):
    """放映厅"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.seekobj = Seek(ios_driver)
        self.homeobj = HomePage(ios_driver)
        self.mvobj = MovieDetails(ios_driver)

    def test_1(self):
        """
        进入搜索页面执行搜索用例
        :return:
        """
        time.sleep(10)
        self.homeobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().click()
        time.sleep(2)
        self.seekobj.seek_button().send_keys('一拳超人')
        time.sleep(2)
        self.seekobj.iphoneseek_button().click()
        time.sleep(2)
        self.seekobj.fristseekmovie_button()
        self.mvobj.yqcrtitle_button()
        self.mvobj.close_button().click()
        self.seekobj.cancel_button().click()






