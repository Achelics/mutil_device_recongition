#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/05'

from config_parser import Config
import MySQLdb
import json

__BRAND_MODEL_LIST = list()


def insert_brand_model():
    config_file = r"D:\Users\Achelics\liu_project\mutil_device_recongition\handle_brand_information\database_config.ini"
    settion = "MyDataBase"
    db_config = Config(config_file, settion)

    url = db_config.get("url")
    user = db_config.get("user")
    pawd = db_config.get("pawd")
    database = db_config.get("database")

    try:
        # open the database
        conn = MySQLdb.connect(url, user, pawd, database)
        # Using the cursor() method to get the operate cursor.
        cursor = conn.cursor()
        for brand_model in __BRAND_MODEL_LIST:
            default_sql = "insert into iie_brand_model(brand, model, category) values('%s', '%s', '%s')" % \
                          (brand_model["Brand"], brand_model["Model"], brand_model["type"])
            cursor.execute(default_sql)
        # 获取所有结果
        conn.commit()
        # 关闭指针
        cursor.close()
        # 关闭数据库连接
        conn.close()
    except MySQLdb.Error, e:
        print("MySQL Error:%s" % str(e))
        print("插入数据库失败")

def init_brand_model(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            __BRAND_MODEL_LIST.append(new_line)
    f.close()


if __name__ == '__main__':
    monitor_file_name = r"F:\mutil_result\final_brand_model\monitor_brand_model_single.json"
    router_file_name = r"F:\mutil_result\final_brand_model\router_brand_model_single.json"

    # init_brand_model(monitor_file_name)
    # print("初始化完成")
    # insert_brand_model()

    # init_brand_model(router_file_name)
    # print("初始化完成")
    # insert_brand_model()


