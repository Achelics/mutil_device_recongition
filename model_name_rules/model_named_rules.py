#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'Achelics'
__date__ = '2017-06-05'

import MySQLdb
import copy

__MODEL_RULES = list()


def __get_model_rules(model_name):
    model_rules = dict()
    model_rules["device_type_1"] = "Monitor"
    with open(model_name, "r") as f:
        for line in f:
            data = line.strip("\r\n")
            if '##' in data:
                model_rules["device_type_2"] = data.split("##")[-1].strip()
                if model_rules["device_type_2"] == 'Switch':
                    model_rules["device_type_1"] = 'Network Equipment'
            elif ('#' in data) and ('##' not in data):
                model_rules["brand"] = data.split("#")[-1].strip()
            elif '```' in data:
                continue
            else:
                model_rules["model_rules"] = data.strip()
                fully_model_rules = copy.deepcopy(model_rules)
                __MODEL_RULES.append(fully_model_rules)


def insert_model_rules():
    url = "10.10.12.207"
    user = "root"
    pawd = "cyberpecker"
    database = "cyberpecker"

    try:
        # open the database
        conn = MySQLdb.connect(url, user, pawd, database)
        # Using the cursor() method to get the operate cursor.
        cursor = conn.cursor()
        for brand_rules in __MODEL_RULES:
            default_sql = "insert into iie_model_rules(device_type_1, device_type_2, brand, model_rules) values('%s', '%s', '%s', '%s')" % (
                brand_rules['device_type_1'], brand_rules['device_type_2'], brand_rules['brand'], brand_rules['model_rules'])
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
    model_name = '/home/achelics/work/data_analysis/mutil_device_recongition/model_name_rules/name_rules.md'
    __get_model_rules(model_name)
    print __MODEL_RULES
    insert_model_rules()