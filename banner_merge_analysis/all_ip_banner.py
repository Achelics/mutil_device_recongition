#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/15'
import json as _json
import multiprocessing
import os
import sys

IP_LIST = list()


def get_all_ip(raw_file_name, result_file_name, flag_num=4):
    result_file = open(result_file_name, 'w')
    with open(raw_file_name, 'r') as f:
        for line in f:
            data = line.strip('\n').strip(',').split(',')
            ip = data[0]
            count_num = 0
            for i in range(0, flag_num):
                count_num += int(data[i+1])
            if count_num == flag_num:
                result_file.write(ip + '\n')
                IP_LIST.append(ip)
    f.close()
    result_file.close()


def get_ip_json(banner_file_name, result_file_name, ip_list):
    result_file = open(result_file_name, 'w')
    print ip_list
    sys.stdout.flush()
    with open(banner_file_name, 'r') as f:
        for line in f:
            data = _json.loads(line.strip('\n'))
            ip = data['ip']
            if ip in ip_list:
                result_file.write(line)
    f.close()
    result_file.close()


if __name__ == '__main__':
    ip_raw_file_name = r'F:\mutil_result\five_protocol\ip_maeked_compare.txt'
    ip_all_result_name = r'F:\mutil_result\five_protocol\five_protocol_all\ip_list.txt'
    get_all_ip(ip_raw_file_name, ip_all_result_name, 5)
    raw_dir = r'F:\mutil_result\five_protocol'
    result_dir = r'F:\mutil_result\five_protocol\five_protocol_all'
    banner_name = ['banner21.json', 'banner22.json', 'banner23.json', 'banner80.json', 'banner554.json']
    for banner in banner_name:
        banner_file_name = os.path.join(raw_dir, banner)
        result_file_name = os.path.join(result_dir, banner)
        process = multiprocessing.Process(target=get_ip_json, args=(banner_file_name, result_file_name, IP_LIST))
        process.start()




