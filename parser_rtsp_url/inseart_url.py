#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = ''
__date__ = ''

import MySQLdb


URL_BRAND_LIST = list()


def __get_url_list():
    file_name = "/home/achelics/work/data_analysis/mutil_device_recongition/parser_rtsp_url/rtsp_url_map_only.ini"
    with open(file_name, 'r') as f:
        for line in f:
            data = line.strip('\r\n').split('=')
            URL_BRAND_LIST.append(data)
    f.close()


def inseart_urt():
    url = "10.10.12.207"
    user = "root"
    pawd = "cyberpecker"
    database = "cyberpecker"

    try:
        # open the database
        conn = MySQLdb.connect(url, user, pawd, database)
        # Using the cursor() method to get the operate cursor.
        cursor = conn.cursor()
        for brand_type in URL_BRAND_LIST:
            print brand_type
            default_sql = "insert into brand_rtsp_url(brand, rtsp_url) values('%s', '%s')" % (brand_type[0], brand_type[1])
            cursor.execute(default_sql)
        # 获取所有结果
        conn.commit()
        # 关闭指针
        cursor.close()
        # 关闭数据库连接
        conn.close()
    except MySQLdb.Error, e:
        print("MySQL Error:%s" % str(e))


__get_url_list()
inseart_urt()
