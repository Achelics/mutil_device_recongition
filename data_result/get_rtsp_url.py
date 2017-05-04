#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017-04-26'

import json as _json


def filter_rtsp_url(raw_file_name="", result_file_name=""):
    result_file = open(result_file_name, "a")
    with open(raw_file_name, "r") as raw_file:
        for raw_line in raw_file:
            raw_data = _json.dumps(raw_line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            rtsp_url = eval_raw_data["RTSP_URL"][0]
            if "[Suggest]" not in  rtsp_url:
                result_file.write(raw_line)
    raw_file.close()
    result_file.close()


def get_rtsp_url(raw_file_name="", result_file_name=""):
    url_list = list()
    with open(raw_file_name, "r") as raw_file:
        for raw_line in raw_file:
            brand_url = dict()
            raw_data = _json.dumps(raw_line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"][0]
            rtsp_url = eval_raw_data["RTSP_URL"][0]
            brand_url["Brand"] = brand
            brand_url["RTSP_URL"] = rtsp_url
            url_list.append(brand_url)
    raw_file.close()
    result_file = open(result_file_name, "a")

    single_brand_list = __remove_2duplicate(url_list)

    rtsp_set = set()
    for brand_url in single_brand_list:
        brand = brand_url["Brand"]
        url = brand_url["RTSP_URL"].split("//")[1]
        rtsp_url = ""
        if "/" in url:
            url_split_list = url.split("/")[1:]
            if len(url_split_list) > 1:
                for url_split in url_split_list:
                    rtsp_url += (url_split + "/")
            else:
                rtsp_url = "/"
        else:
            rtsp_url = "/"
        rtsp_set.add(brand + "=" + rtsp_url)

    for rtsp in rtsp_set:
        result_file.write(rtsp + "\n")

    result_file.close()

# 根据字典前两个值进行去重
def __remove_2duplicate(dict_list):
    seen = set()
    new_dict_list = []
    for dict in dict_list:
        t_dict = {'Brand': dict['Brand'], 'RTSP_URL': dict['RTSP_URL']}
        t_tup = tuple(t_dict.items())
        if t_tup not in seen:
            seen.add(t_tup)
            new_dict_list.append(dict)
    return new_dict_list


# 只获取有特殊路径的品牌路径信息
def get_rtsp_url_mutil(raw_file_name="", result_file_name=""):
    result_file = open(result_file_name, "a")
    with open(raw_file_name, "r") as raw_file:
        for raw_line in raw_file:
            url = raw_line.strip("\n").split("=")[1]
            if "/" == url:
                pass
            else:
                result_file.write(raw_line)
    raw_file.close()
    result_file.close()


if __name__ == '__main__':
    raw_file_name = r"F:\mutil_result\device_tag_ll\brand_list1\geniusvision\geniusvision_RTSPURL.json"
    result_file_name = r"F:\mutil_result\rtsp_url\rtsp_url.json"
    config_file_name = r"F:\mutil_result\rtsp_url\rtsp_url_map.ini"
    only_config_file_name = r"F:\mutil_result\rtsp_url\rtsp_url_map_only.ini"
    # filter_rtsp_url(raw_file_name, result_file_name)
    # get_rtsp_url(result_file_name, config_file_name)

    get_rtsp_url_mutil(config_file_name, only_config_file_name)

