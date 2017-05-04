#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/18'

import json as _json
import re as _re
import multiprocessing
import os as _os

class ValidityJson(multiprocessing.Process):
    """
        获取合法json数据格式的进程
    """
    def __init__(self, path, raw_file_name, ip_file_name):
        multiprocessing.Process.__init__(self)
        self.raw_file_name = _os.path.join(path, raw_file_name)
        self.result_file_name = _os.path.join(path, "validity_" + raw_file_name)
        self.ip_file_name = _os.path.join(path, ip_file_name)

    def run(self):
        self.get_validity_json()

    def get_validity_json(self):
        json_pattern = "\\{.*\\}"
        result_file = open(self.result_file_name, 'a')
        ip_file = open(self.ip_file_name, 'a')
        num_count = 0
        with open(self.raw_file_name, 'r') as f:
            for line in f:
                data = None
                try:
                    pattern = _re.compile(json_pattern)
                    matcher = pattern.search(line.strip('\r\n'))
                    if matcher:
                        data = _json.loads(matcher.group(0), strict=False)
                        if 'ip' in data:
                            num_count += 1
                            result_file.write(_json.dumps(data, encoding="UTF-8", ensure_ascii=False) + '\n')
                            ip = data['ip']
                            ip_file.write(ip + '\n')
                except Exception, e:
                    print '----> ' + str(data) + str(e)

        f.close()
        result_file.close()
        ip_file.close()
        print str(self.raw_file_name) + ' 的个数为：' + str(num_count)
