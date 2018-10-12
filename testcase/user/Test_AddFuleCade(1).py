import unittest
import requests
from lib.read_excel import get_data
import json
import sys
sys.path.append("../..")

from config.config import *

# 准备数据
class Test_Add_Fule_Cade(unittest.TestCase):
    url = "http: // 115.28.108.130: 8080 / gasStation / process"
    def test_add_fule_cade_mormal(self):
        data_list = get_data(data_file,'TestAddFuleCade','test_add_fule_cade_mormal')  #获得数据，并且获得的数据是list格式
        url = data_list[1]
        # data=json.loads(data_list[3]) #json格式的字符串转化为字典
        data=data_list[3] #json格式的字符串转化为字典
        expect_res = json.loads(data_list[4]) #期望结果
        res = requests.post(url=url, data = json.loads(data_list[3])) # 返回结果
        # res = requests.post(url=url, data = data_list[3]) # 返回结果
        # self.assertDictEqual(res.json(),expect_res) # 断言

        logging.info("测试用例：{}".format("test_add_fule_cade_mormal"))
        logging.info("请求url：{}".format(url))
        logging.info("请求数据：{}".format(data))
        logging.info("期望结果：{}".format(res))


    def test_add_fule_cade_failed(self):
        data_list = get_data(data_file, "TestAddFuleCade", "test_add_fule_cade_failed")  # 数据
        url = data_list[1]
        data = data_list[3]  # json格式的字符串转化为字典
        expect_res = json.loads(data_list[4]) # 期望结果
        res = requests.post(url=url, data=json.loads(data_list[3]))  # 返回结果
        # res = requests.post(url=url, data=data_list[3])  # 返回结果
        # self.assertDictEqual(res.json(), expect_res) # 断言

        logging.info("测试用例：{}".format("test_add_fule_cade_failed"))
        logging.info("请求url：{}".format(url))
        logging.info("请求数据：{}".format(data))
        logging.info("期望结果：{}".format(res))

if __name__ == "__main__":
    unittest.main()