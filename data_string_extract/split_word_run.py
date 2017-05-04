#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/24'

import os as _os
from parse_short_banner import ParseBannerProcess

if __name__ == '__main__':
    raw_path = r"F:\mutil_result\five_protocol_50\data_process"

    raw_file_name = [
                        _os.path.join(raw_path, "banner21_stringok.txt"),
                        _os.path.join(raw_path, "banner22_stringok.txt"),
                        _os.path.join(raw_path, "banner23_stringok.txt"),
                        _os.path.join(raw_path, "banner554_stringok.txt")
                    ]

    result_file_name = [
                        _os.path.join(raw_path, "banner21_short.txt"),
                        _os.path.join(raw_path, "banner22_short.txt"),
                        _os.path.join(raw_path, "banner23_short.txt"),
                        _os.path.join(raw_path, "banner554_short.txt")
                       ]

    for i in range(1):
        psb = ParseBannerProcess(raw_file_name[i], result_file_name[i])
        psb.start()