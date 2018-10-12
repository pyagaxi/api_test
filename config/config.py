import logging
import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路径，使用绝对路径不容易出错
data_file = os.path.join(prj_path,'data','data.xlsx')  # 数据路径 用join可以跨平台使用
testcase_path = os.path.join(prj_path,'testcase')  #用例路径
report_file = os.path.join(prj_path,'report','report.html')  #用例路径
log_file = os.path.join(prj_path,'log','log.txt')  #日志路径

# 全局log配置
logging.basicConfig(level=logging.INFO, #设置为调试模式
                    format = '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a")  #a每次追加

# 数据库配置

db_host = "115.28.108.130"
db_user = "test"
db_passwd = "123456"
db_port = 3306
db = "api_test"


# 邮件配置
smtp_server = "smtp.163.com"
smtp_user = "ivan-me@163.com"
smtp_password = "hanzhichao123"
sender = "ivan-me@163.com"
receiver = "1334650360@qq.com"
subject = "接口测试报告"
email_body = "测试完成，请查看测试报告"

if __name__ == '__main__':
    logging.info("haha")
    # logging.error("error")

