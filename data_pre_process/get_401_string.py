#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/24'

import os as _os
import json as _json
import multiprocessing
import sys as _sys
reload(_sys)
_sys.setdefaultencoding("utf-8")

def split_http_web(raw_file_path="", raw_file_name="", result_path=""):
    """
        根据http协议的状态码得到分割结果
    :param raw_file_path: 原始文件所在路径
    :param raw_file_name: 原始文件名称
    :param result_path: 结果文件路径
    :param status_code: 状态码
    :return:
    """
    status_file_name = raw_file_name.split(".")[0] + "_string" + ".json"
    status_file = open(_os.path.join(result_path, status_file_name), "a")
    num_flag = 0
    with open(_os.path.join(raw_file_path, raw_file_name), "r") as f:
        for line in f:
            num_flag += 1
            raw_data = _json.loads(line.strip('\n'))
            if "data" in raw_data:
                if "http" in raw_data["data"]:
                    if "response" in raw_data["data"]["http"]:
                        response = raw_data["data"]["http"]["response"]
                        if "headers" in response:
                            headers = response["headers"]
                            if "www_authenticate" in headers:
                                relam = headers["www_authenticate"][0]
                                # result = str(num_flag) + "\t" + relam
                                status_file.write(relam + "\n")
    f.close()
    status_file.close()

if __name__ == '__main__':
    raw_file_path = r"D:\source_data"
    result_file_path = r"F:\mutil_result\401_brand_analysis"
    http_kw = dict()
    http_kw["raw_file_path"] = raw_file_path
    http_kw["raw_file_name"] = "80-http-banner-zgrab-results-401_0"
    http_kw["result_path"] = result_file_path

    http_p = multiprocessing.Process(target=split_http_web, kwargs=http_kw)
    http_p.start()