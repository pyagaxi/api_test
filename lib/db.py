import pymysql
import sys
sys.path.append("..") #提升其路径到项目路径下

from config.config import *


def get_db_con():
    conn = pymysql.connect(host = db_host,user = db_user,passwd = db_passwd,db = db,port = db_port,charset = "utf8")
    return conn

def query_db(sql):
    logging.debug(sql)
    con = get_db_con()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    result = cur.execute(sql)
    logging.debug(result)
    cur.close()
    con.close()
    return result

def change_db(sql):
    logging.debug(sql)
    con = get_db_con()
    cur = con.cursor()
    cur.excute(sql)
    con.commit()

def add_user(name,passwd):
    sql = "insert into user (name,passwd) values ('{}','{}')".format(name,passwd)
    change_db(sql)

def check_user(name):
    sql = "select * from user where name = '{}'".format(name)
    return query_db(sql)

def del_user(name):
    sql = "delete from user where name = '{}'".format(name)
    change_db(sql)

if __name__ == "__main__":
    print(check_user('lisi'))