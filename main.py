import os
import unittest
import time
import yagmail
# from common.HTMLTestRunner import HTMLTestRunner





#引入测试模块
from testcases import test_login
# from testcases import test_meirituijian
# from testcases import test_wonderfulguide
# from testcases import test_lookmovies
# from testcases import test_review
# from testcases import test_wonderful
# from testcases import test_likemovies
# from testcases import test_mymovies
# from testcases import test_seek
# from testcases import test_off_linecache
# from testcases import test_member
# from testcases import test_nangualab
# from testcases import test_store
# from testcases import test_ado
# from testcases import test_logout
# from testcases import test_overdue



#创建测试集

suite = unittest.TestSuite()
loader = unittest.TestLoader()
#添加测试用例到测试集

suite.addTests(loader.loadTestsFromModule(test_login))#登录页面测试用例
# suite.addTests(loader.loadTestsFromModule(test_meirituijian))#每日推荐用例
# suite.addTests(loader.loadTestsFromModule(test_wonderfulguide))#精彩导视用例和播放
# suite.addTests(loader.loadTestsFromModule(test_lookmovies))#继续观看用例
# suite.addTests(loader.loadTestsFromModule(test_review))#影评用例
# suite.addTests(loader.loadTestsFromModule(test_wonderful))#精彩小视频用例
# suite.addTests(loader.loadTestsFromModule(test_likemovies))#喜欢影视用例
# suite.addTests(loader.loadTestsFromModule(test_mymovies))#我的片单用例
# suite.addTests(loader.loadTestsFromModule(test_seek))#搜索用例
# suite.addTests(loader.loadTestsFromModule(test_off_linecache))#离线缓存用例
# suite.addTests(loader.loadTestsFromModule(test_member))#我的会员
# # suite.addTests(loader.loadTestsFromModule(test_nangualab))#南瓜实验室 倍速  现在去掉了南瓜实验室的倍速 故去掉这个功能
# suite.addTests(loader.loadTestsFromModule(test_store))#南瓜商城
# suite.addTests(loader.loadTestsFromModule(test_ado))#青少年模式
# suite.addTests(loader.loadTestsFromModule(test_logout))#退出登录
# suite.addTests(loader.loadTestsFromModule(test_overdue))#过期用例


#执行测试用例 （调试展示）
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)





# now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
# report_html = "./report/" + now_time + "result.html"
# fp = open(report_html, "wb")
#
# runner = HTMLTestRunner(
#     stream = fp,
#     verbosity=2,
#     title="南瓜电影ui测试",
#     description="环境：正式环境 , version：5.2.2 ,机型：苹果6sp，系统：14。4"
#     )
# runner.run(suite)
# fp.close()

