#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/05'

import MySQLdb
from config_parser import Config
__RAW_BRAND_LIST = list()
__BRAND_LIST = list()


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


def insert_brand():
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
        for brand_type in __RAW_BRAND_LIST:
            if str(brand_type[0]).strip().upper() not in __BRAND_LIST:
                print brand_type
                default_sql = "insert into iie_brand(en_name, product_type) values('%s', '%s')" % (brand_type[0], brand_type[1])
                cursor.execute(default_sql)
        # 获取所有结果
        conn.commit()
        # 关闭指针
        cursor.close()
        # 关闭数据库连接
        conn.close()
    except MySQLdb.Error, e:
        print("MySQL Error:%s" % str(e))


def get_brand():
    brand_file_name = r"F:\mutil_result\final_brand_model\brand.json"
    with open(brand_file_name, "r") as f:
        for line in f:
            brand_type = []
            brand = line.strip("\n").split("\t")[0]
            device_type = line.strip("\n").split("\t")[1].strip(",")
            brand_type.append(brand)
            brand_type.append(device_type)
            __RAW_BRAND_LIST.append(brand_type)
    f.close()

if __name__ == '__main__':
    __init_brand_list()
    print("初始化数据库品牌完毕")
    get_brand()
    print("获取原始品牌完毕")
    insert_brand()
    print("插入原始数据库品牌结束")