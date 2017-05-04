#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

if __name__ == '__main__':

    file_name = r"F:\mutil_result\five_protocol_50\banner80.json"
    result_name = r"F:\mutil_result\five_protocol_50\banner80_100.json"
    file = open(result_name, "a+")
    nux_num = 0
    with open(file_name, "r") as f:
        for line in f:
            if nux_num >= 100:
                break
            nux_num +=1
            file.write(line)
    f.close()
    file.close()