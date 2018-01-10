from tools.net_tools import my_session, _get_headers
from tools.selenium_tools import _get_driver
from config import config
import os

"""
1. webdriver模拟拉到页面最底部，获取关键字页面源码内容-->转成bs对象-->匹配到问题的网址，标题
2. 检测网址是否已经存在，不存在就黑白名单过滤，
3. 将网址信息添加到数组，将问题信息(包含网址链接，标题等内容)添加到队列 


4. 后面的事就是另一个进程从队列里获取问题，读取解析问题，保存到数据库中
"""

urll = 'https://www.zhihu.com/topic/20011035/top-answers?page=1'

session = my_session()
session.headers = _get_headers()
ROOTURL = config.get('root_url')
basedir = os.path.abspath(os.path.dirname(__name__))

# driver = _get_driver()
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(config.get('start_url'))
print(driver.page_source)

