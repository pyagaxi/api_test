import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email_HAN import send_email
from config.config import *


logging.info('测试开始')
suite = unittest.defaultTestLoader.discover(testcase_path) #运行所有用例

# 上下文结构题，执行完文件，即可关闭文件
with open(report_file,"wb") as f:
    HTMLTestRunner(stream=f,title="test report",description="haha").run(suite)
# logging.info('测试结束')

send_email(report_file)
logging.info("邮件已发送")
logging.info('测试结束')



