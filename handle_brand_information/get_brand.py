#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/05'
import json
import os
__BRAND_SET = set()
__RAW_BRAND_LIST = list()


def get_brand_set(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            __BRAND_SET.add(new_line["Brand"])
    f.close()


def get_raw_brand(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            __BRAND_SET.add(str(new_line["Brand"]).strip())
    f.close()


def __ingore_letter():
    brand_upper_list = set()
    for brand in __BRAND_SET:
        if str(brand).upper() not in brand_upper_list:
            __RAW_BRAND_LIST.append(brand)
        brand_upper_list.add(str(brand).upper())


def result_generate(result_file_name):
    result_file = open(result_file_name, "a")
    for brand in __RAW_BRAND_LIST:
        result_file.write(brand)
        result_file.write("\n")
    result_file.close()


if __name__ == '__main__':
    # monitor_file_name = r"F:\mutil_result\final_brand_model\monitor_brand_model_single.json"
    # monitor_brand_first = r"F:\mutil_result\raw_brand_file\monitor_brand_1.json"
    # monitor_brand_second = r"F:\mutil_result\raw_brand_file\monitor_brand_2.json"
    # get_brand_set(monitor_file_name)
    # print("获取原始数据集结束--->monitor")
    # get_raw_brand(monitor_brand_first)
    # print("获取原始品牌集结束-first--->monitor")
    # get_raw_brand(monitor_brand_first)
    # print("获取原始品牌集结束-second--->monitor")
    # __ingore_letter()
    # print("品牌数据集去重结束--->monitor")
    # monitor_result_name = r"F:\mutil_result\final_brand_model\monitor_brand.json"
    # if os.path.isfile(monitor_result_name):
    #     os.remove(monitor_result_name)
    # result_generate(monitor_result_name)
    # print("品牌数据集获取成功--->monitor")

    router_file_name = r"F:\mutil_result\final_brand_model\router_brand_model_single.json"
    router_brand_name_first = r"F:\mutil_result\raw_brand_file\Routerbrand_1.json"
    router_brand_name_second = r"F:\mutil_result\raw_brand_file\Routerbrand_2.json"
    get_brand_set(router_file_name)
    print("获取原始数据集结束--->router")
    get_raw_brand(router_brand_name_first)
    print("获取原始品牌集结束-first--->router")
    get_raw_brand(router_brand_name_second)
    print("获取原始品牌集结束-second--->router")
    __ingore_letter()
    print("品牌数据集去重结束--->router")
    monitor_result_name = r"F:\mutil_result\final_brand_model\router_brand.json"
    if os.path.isfile(monitor_result_name):
        os.remove(monitor_result_name)
    result_generate(monitor_result_name)
    print("品牌数据集获取成功--->router")