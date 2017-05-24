#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/16'

from data_pre_process.split_banner_man import *
import os
import json as _json


def get_ip_banner(path, filename, protocol_validity_json):
    """
        提取ip和标语
    :param path: 标语文件所在路径
    :param filename: 标语文件名称
    :param protocol_validity_json: 标语文件合法提取函数
    :return:
    """
    file_name = os.path.join(path, filename)
    resultname = filename.split('.')[0] + '_clear.json'
    result_name = os.path.join(path, resultname)
    result_file = open(result_name, 'a')
    with open(file_name, 'r') as f:
        for line in f:
            raw_data = _json.loads(line.strip('\n'), strict=False)
            ip = raw_data['ip']
            result = protocol_validity_json(raw_data)
            if result["banner_flag"]:
                banner = result["banner_string"]
                result_file.write(str(ip) + '卍' + str(banner) + '\n')
            else:
                result_file.write(str(ip) + '\n')
    f.close()
    result_file.close()


def get_only_banner(path, filename):
    """
        提取ip存在的标语
    :param path: 标语文件所在路径
    :param filename: 标语文件名称
    :return:
    """
    file_name = os.path.join(path, filename)
    resultname = filename.split('.')[0] + '_only_banner.json'
    result_name = os.path.join(path, resultname)
    result_file = open(result_name, 'a')
    with open(file_name, 'r') as f:
        for line in f:
            raw_data = line.strip('\n')
            if '卍' in raw_data:
                result_file.write(line)
    f.close()
    result_file.close()


if __name__ == '__main__':
    path = r'F:\mutil_result\five_protocol\five_protocol_all'
    banner_name = ['banner21.json', 'banner22.json', 'banner23.json', 'banner80.json', 'banner554.json']
    protocol_json_list = [ftp_validity_json, ssh_validity_json, telnet_validity_json, http_validity_json, rtsp_validity_json]
    clear_name = ['banner21_clear.json', 'banner22_clear.json', 'banner23_clear.json', 'banner80_clear.json', 'banner554_clear.json']
    # for i in range(0, len(clear_name)):
    #     process = multiprocessing.Process(target=get_ip_banner, args=(path, banner_name[i], protocol_json_list[i]))
    #     process.start()

    for i in range(0, len(clear_name)):
        process = multiprocessing.Process(target=get_only_banner, args=(path, clear_name[i]))
        process.start()


