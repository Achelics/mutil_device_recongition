#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/25'


if __name__ == '__main__':

    brand = "MikroTik"
    file_name = r"F:\mutil_result\five_protocol_50\data_process\banner21_short.txt"
    num_flag = 0
    with open(file_name, "r") as f:
        for line in f:
            if brand.upper() in line.upper():
                num_flag += 1
    f.close()
    print num_flag