#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/04'

import MySQLdb
import json
from config_parser import Config

__BRAND_LIST = list()
__RAW_BRAND_LIST = list()


def __init_brand_list():
    config_file = r"D:\Users\Achelics\liu_project\mutil_device_recongition\handle_brand_information\database_config.ini"
    settion = "MyDataBase"
    db_config = Config(config_file, settion)

    url = db_config.get("url")
    user = db_config.get("user")
    pawd = db_config.get("pawd")
    database = db_config.get("database")

    try:
        # open the database
        db = MySQLdb.connect(url, user, pawd, database)
        # Using the cursor() method to get the operate cursor.
        cursor = db.cursor()
        # SQL select by vulflag
        sql_default = "SELECT DISTINCT(en_name) FROM iie_brand ORDER BY LENGTH(en_name) DESC"
        # excute SQL sentence
        cursor.execute(sql_default)
        # Get the all record
        default_results = cursor.fetchall()
        for row in default_results:
            __BRAND_LIST.append(str(row[0]).upper())
        # 关闭数据库连接
        db.close()
    except MySQLdb.Error, e:
        print("MySQL Error:%s" % str(e))


def get_brand(raw_model_name, raw_brand_name):
    brand_set = set()
    with open(raw_model_name, "r") as model_f:
        for line in model_f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            model_brand = new_line["Brand"]
            brand_set.add(str(model_brand).strip())
    model_f.close()

    with open(raw_brand_name, "r") as brand_f:
        for line in brand_f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            brand_brand = new_line["Brand"]
            brand_set.add(str(brand_brand).strip())
    brand_f.close()
    brand_upper_list = set()

    for brand in brand_set:
        if str(brand).upper() not in brand_upper_list:
            __RAW_BRAND_LIST.append(brand)
        brand_upper_list.add(str(brand).upper())


def insert_brand(product_type):
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
        for brand in __RAW_BRAND_LIST:
            if str(brand).strip().upper() not in __BRAND_LIST:
                print brand, product_type
                default_sql = "insert into iie_brand(en_name, product_type) values('%s', '%s')" % (brand, product_type)
                cursor.execute(default_sql)
        # 获取所有结果
        conn.commit()
        # 关闭指针
        cursor.close()
        # 关闭数据库连接
        conn.close()
    except MySQLdb.Error, e:
        print("MySQL Error:%s" % str(e))


if __name__ == '__main__':
    # raw_model_name = r"F:\mutil_result\device_tag_ll\brand_model\model.json"
    # raw_brand_name = r"F:\mutil_result\device_tag_ll\brand_model\brand.json"
    # product_type = "Monitor"
    raw_model_name = r"F:\mutil_result\device_tag_ll\brand_model\Routermodel.json"
    raw_brand_name = r"F:\mutil_result\device_tag_ll\brand_model\Routerbrand.json"
    product_type = "Router"

    __init_brand_list()
    # print __BRAND_LIST
    get_brand(raw_model_name, raw_brand_name)
    # print __RAW_BRAND_LIST
    insert_brand(product_type)
    # print __BRAND_LIST


