#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/24'

import re as _re
import sys as _sys
import json as _json
reload(_sys)
_sys.setdefaultencoding("utf-8")
import multiprocessing

class ParseBannerProcess(multiprocessing.Process):
    """
        ftp协议的预处理
    """
    def __init__(self, raw_file_name, result_file_name):
        multiprocessing.Process.__init__(self)
        self.raw_file_name = raw_file_name
        self.result_file_name = result_file_name
        self.status_code = "220"

    def get_word(self, raw_string):
        pattern = r"[\s+\{\}\\\=\>\<\|\[\]\-\!\/_,$%^*+\"\']+|[+——！，。？、~@#￥%……&*（）]+"
        raw_string = str(raw_string).decode("utf-8")
        result_string = _re.sub(pattern.decode("utf8"),
                                " ".decode("utf8"), raw_string)
        if self.status_code in result_string:
            return result_string.split(self.status_code)[1]
        else:
            return result_string

    def run(self):
        result_file = open(self.result_file_name, "a")
        with open(self.raw_file_name, "r") as f:
            for line in f:
                raw_banner = _json.loads(line.strip("\n"))
                raw_data = raw_banner["raw_banner"]
                result = self.get_word(raw_data)
                result_file.write(str(result) + "\n")
        f.close()
        result_file.close()
