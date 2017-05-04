#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/18'

import multiprocessing
from get_validity_json import ValidityJson

if __name__ == '__main__':
    raw_path = "F:\\mutil_result\\forth_protocol"
    raw_json_list = ["banner21.json", "banner23.json", "banner80.json", "banner554.json"]
    ip_list = ["ip_1.txt", "ip_3.txt", "ip_4.txt", "ip_5.txt"]
    pool = multiprocessing.Pool(processes=4)

    for i in range(len(raw_json_list)):
        validityJson = ValidityJson(raw_path, raw_json_list[i], ip_list[i])
        pool.apply_async(validityJson.get_validity_json())

    print "Waiting for all subprocesses done..."
    pool.close()
    pool.join()  # 调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待素有子进程结束
    print "All subprocesses done."