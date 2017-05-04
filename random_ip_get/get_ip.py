#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/18'

from netaddr import *


def get_random_ip(raw_file_name="", result_file_name="", num=100):
    result_file = open(result_file_name, 'a')
    i = 0
    with open(raw_file_name, 'r') as f:
        for line in f:
            if i % num == 0:
                result_file.write(line)
            i += 1
    f.close()
    result_file.close()


def get_random_ip_num(result_file="", ip_num=""):
    raw_file = result_file
    num_file = open(ip_num, 'a')
    ALL_NUM = 0
    with open(raw_file, 'r') as f:
        for line in f:
            cidr_ip = line.strip('\n')
            ip_list = IPNetwork(cidr_ip)
            ip_num = list(ip_list).__len__()
            num_file.write(str(ip_num) + '\n')
            ALL_NUM += ip_num
    num_file.write(str(ALL_NUM))
    f.close()
    num_file.close()