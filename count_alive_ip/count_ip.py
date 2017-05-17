#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'AChelics'
__Date__ = '2017/04/18'

import os as _os
import re as _re
import multiprocessing

def merge_ip_file(ip_path, tmp_file_name, ip_result):
    """
        将多个ip文件合并成单个ip文件，并且去重
    :param ip_path: ip文件所在路径
    :param tmp_file_name: 合并之后的ip临时文件
    :param ip_result: 去重之后的ip文件
    :return:
    """
    tmp_file = open(tmp_file_name, 'a')
    for parent, dirnames, filenames in _os.walk(ip_path):
        for filename in filenames:
            raw_file = open(_os.path.join(ip_path, filename), 'r')
            tmp_file.write(raw_file.read())
            raw_file.close()
    tmp_file.close()
    print "合并文件结束"

    rFile = open(tmp_file_name, 'r')
    wFile = open(ip_result, 'w')
    allLine = rFile.readlines()
    rFile.close()
    s = set()
    for i in allLine:
        s.add(i)
    for i in s:
        wFile.write(i)
    rFile.close()
    wFile.close()
    # open(ip_result, 'w').write(''.join(set(open(tmp_file_name).readlines())))
    print "文件去重结束"

def in_string(sub_string, all_string):
    """
        判断子字符串是否在主字符串中，返回0或者1
    :param sub_string: 子字符串
    :param all_string: 主字符串
    :return:
    """
    return '1' if sub_string in all_string else '0'


def writer(string, ip_marked):
    file = open(ip_marked, 'a')
    file.write(string + '\n')
    file.close()

def marked_ip_file(ip_path, ip_result, ip_marked):
    """
        根据单个协议ip文件，对所有的ip进行开放协议标记；标记格式为： ip,1,0,0,1,1,
    :param ip_path: 单个协议ip文件所在的路径
    :param ip_result: 所有存活ip文件
    :param ip_marked: 标记好的ip文件
    :return:
    """
    marked_file = open(ip_marked, 'a')
    list_name = ["ip_21.txt", "ip_22.txt", "ip_23.txt", "ip_80.txt", "ip_554.txt"]

    with open(ip_result, 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            result_marked = ip + ','
            # 每个文件使用进程进行运算
            for filename in list_name:
                fin = open(_os.path.join(ip_path, filename), 'r')
                finlines = fin.read()
                if ip in finlines:
                    result_marked += '1' + ','
                else:
                    result_marked += '0' + ','
            # print result_marked
            marked_file.write(result_marked + '\n')
    f.close()
    marked_file.close()

    # print "ip文件标记结束"

if __name__ == '__main__':
    ip_path = r'F:\mutil_result\five_protocol_50'
    # tmp_file_name = "F:\\mutil_result\\five_protocol_50\\ip_tmp.txt"
    ip_result_name = "F:\\mutil_result\\five_protocol_50\\ip_result.txt"
    ip_marked_name = "F:\\mutil_result\\five_protocol_50\\ip_marked_result.txt"

    # merge_ip_file(ip_path, tmp_file_name, ip_result_name)
    marked_ip_file(ip_path, ip_result_name, ip_marked_name)
