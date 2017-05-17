#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

if __name__ == '__main__':
    ip_set = set()
    with open(r'F:\mutil_result\five_protocol_50\ip_tmp.txt', 'r') as f:
        for line in f:
            ip = line.strip('\n')
            ip_set.add(ip)
    f.close()
    result_file = open(r'F:\mutil_result\five_protocol_50\ip_result.txt', 'a')
    for ip in ip_set:
        result_file.write(ip)
        result_file.write('\n')
    result_file.close()