#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/04'

import json
from general_tools import *
import sys as _sys
import os
__BRAND_MODEL_LIST = []


def get_cleancss_brand_model(raw_file_name, device_type):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            type = new_line["Type"]
            brand_model_dict = dict()
            if type:
                if str(device_type).upper() in str(type[0]).upper():
                    brand_model_dict["Brand"] = str(new_line["Brand"]).strip()
                    brand_model_dict["Model"] = str(new_line["Model"]).strip()
                    brand_model_dict["type"] = device_type
                    __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取cleancss的结果结束"


"""def get_defaultpasword_brand(raw_file_name, device_type):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            type = new_line["Product"]
            brand_model_dict = dict()
            if type:
                if str(device_type).upper() in str(type[0]).upper():
                    brand_model_dict["Brand"] = new_line["Manufactor"]
                    brand_model_dict["Model"] = new_line["Model"]
                    __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取defaultpassword的结果结束"""""


def get_geniusvision_brand_model(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            brand_model_dict = dict()
            brand_model_dict["Brand"] = str(new_line["Brand"][0]).strip()
            brand_model_dict["Model"] = str(new_line["Model"][0]).strip()
            brand_model_dict["type"] = "Monitor"
            __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取geniusvision的结果结束"


def get_ipvm_brand_model(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            brand_model_dict = dict()
            brand_model_dict["Brand"] = str(new_line["Brand"][0]).strip()
            brand_model_dict["Model"] = str(new_line["Model"][0]).strip()
            brand_model_dict["type"] = "Monitor"
            __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取ipvm的结果结束"


def get_portforward_brand_model_router(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            brand_model_dict = dict()
            brand_model_dict["Brand"] = str(new_line["Brand"]).strip()
            model = new_line["Model"]
            brand_model_dict["type"] = "Router"
            if model:
                brand_model_dict["Model"] = str(model[0]).strip()
                __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取portforward的结果结束"


def get_soleratec_brand_model(raw_file_name):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            brand_model_dict = dict()
            brand_model_dict["Brand"] = str(new_line["Company"][0]).strip()
            brand_model_dict["Model"] = str(new_line["Camera_Model"][0]).strip()
            brand_model_dict["type"] = "Monitor"
            __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取soleratec的结果结束"


def get_raw_brand_model(raw_file_name, deviceType):
    with open(raw_file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            brand_model_dict = dict()
            brand_model_dict["Brand"] = str(new_line["Brand"]).strip()
            brand_model_dict["Model"] = str(new_line["Model"]).strip()
            brand_model_dict["type"] = deviceType
            __BRAND_MODEL_LIST.append(brand_model_dict)
    f.close()
    print "获取原始brand的结果结束"


if __name__ == '__main__':
    reload(_sys)
    _sys.setdefaultencoding('utf-8')

    cleancss_name = r"F:\mutil_result\raw_brand_file\cleancss_default_router.json"
    geniusvision_name = r"F:\mutil_result\raw_brand_file\geniusvision_RTSPURL.json"
    ipvm_name = r"F:\mutil_result\raw_brand_file\ipvm_modellist.json"
    portforward_name = r"F:\mutil_result\raw_brand_file\portforward.json"
    soleratec_name = r"F:\mutil_result\raw_brand_file\soleratec_rtsplist.json"
    monitor_model_first = r"F:\mutil_result\raw_brand_file\monitor_model_1.json"
    monitor_model_second = r"F:\mutil_result\raw_brand_file\monitor_model_2.json"

    router_model_first = r"F:\mutil_result\raw_brand_file\Routermodel_1.json"
    router_model_second = r"F:\mutil_result\raw_brand_file\Routermodel_2.json"

    monitor_type_tag = "Monitor"
    router_type_tag = "Router"

    get_geniusvision_brand_model(geniusvision_name)
    print("获取geniuvision品牌和型号结束——》Monitor")
    get_ipvm_brand_model(ipvm_name)
    print("获取ipvm品牌和型号结束——》Monitor")
    get_soleratec_brand_model(soleratec_name)
    print("获取soleratec品牌和型号结束——》Monitor")
    get_cleancss_brand_model(cleancss_name, monitor_type_tag)
    print("获取cleancss品牌和型号结束——》Monitor")
    get_raw_brand_model(monitor_model_first, monitor_type_tag)
    print("获取原始monitor品牌和型号结束_1_——》Monitor")
    get_raw_brand_model(monitor_model_second, monitor_type_tag)
    print("获取原始monitor品牌和型号结束_2_——》Monitor")
    brand_model_list = remove_2duplicate(__BRAND_MODEL_LIST)
    print("品牌型号去重结束")
    monitor_result_name = r"F:\mutil_result\final_brand_model\monitor_brand_model.json"
    if os.path.isfile(monitor_result_name):
        os.remove(monitor_result_name)
    monitor_result_file = open(monitor_result_name, "a")
    for brand_model in brand_model_list:
        try:
            brand_model_json = json.dumps(brand_model, encoding="UTF-8", ensure_ascii=False)
            monitor_result_file.write(brand_model_json)
            monitor_result_file.write("\n")
        except Exception, e:
            print str(brand_model) + " ...... " + str(e)

    monitor_result_file.close()

    # get_cleancss_brand_model(cleancss_name, router_type_tag)
    # print("获取cleancss品牌和型号结束——》Router")
    # get_portforward_brand_model_router(portforward_name)
    # print("获取portforward品牌和型号结束——》Router")
    # get_raw_brand_model(router_model_first, router_type_tag)
    # print("获取原始monitor品牌和型号结束_1_——》Router")
    # get_raw_brand_model(router_model_second, router_type_tag)
    # print("获取原始monitor品牌和型号结束_2_——》Router")
    # router_result_name = r"F:\mutil_result\final_brand_model\router_brand_model.json"
    # brand_model_list = remove_2duplicate(__BRAND_MODEL_LIST)
    # print("品牌型号去重结束")
    # if os.path.isfile(router_result_name):
    #     os.remove(router_result_name)
    # router_result_file = open(router_result_name, "a")
    # for brand_model in brand_model_list:
    #     try:
    #         brand_model_json = json.dumps(brand_model, encoding="UTF-8", ensure_ascii=False)
    #         router_result_file.write(brand_model_json)
    #         router_result_file.write("\n")
    #     except Exception, e:
    #         print str(brand_model) + " ...... " + str(e)
    #
    # router_result_file.close()








