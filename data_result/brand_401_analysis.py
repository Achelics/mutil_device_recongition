#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

import json as _json
import os as _os
from collections import Counter
import matplotlib.pyplot as plt

def get_brand_count(raw_file_name="", result_file_name=""):
    brand_set = set()
    with open(raw_file_name, "r") as raw_f:
        for raw_line in raw_f:
            raw_data = _json.dumps(raw_line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Output"][0]["brand"]
            brand_set.add(brand)
    raw_f.close()

    result_file = open(result_file_name, "a")
    brand_num = 0
    for brand in brand_set:
        brand_num += 1
        result_file.write(brand + "\n")

    result_file.write(str(brand_num) + "\n")
    result_file.close()


def get_brand_num(raw_file_name="", result_file_name=""):
    brand_list = list()
    with open(raw_file_name, "r") as raw_f:
        for raw_line in raw_f:
            raw_data = _json.dumps(raw_line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Output"][0]["brand"]
            brand_list.append(brand)
    raw_f.close()

    brand_dict = Counter(brand_list).items()
    print brand_dict
    result_file = open(result_file_name, "a")
    num = 0
    for brand_num in brand_dict:
        num += 1
        result_file.write(str(brand_num[0]) + "\t" + str(brand_num[1]) + "\n")

    result_file.write(str(num) + "\n")
    result_file.close()


def show_plot(result_file_name=""):
    brand_list = list()
    brand_num = list()

    with open(result_file_name, "r") as result_f:
        for result_line in result_f:
            brand = result_line.strip("\n").split("\t")[0]
            num = result_line.strip("\n").split("\t")[1]
            brand_list.append(brand)
            brand_num.append(num)
    result_f.close()
    x = range(len(brand_list))
    y = brand_num
    plt.plot(x, y, "-")
    plt.xticks(x, brand_list, rotation=45)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    plt.show()

if __name__ == '__main__':
    raw_file_path= r"F:\mutil_result\401_analysis_result"
    raw_file_name = _os.path.join(raw_file_path, r"include_string_brand.json")
    result_file_name = _os.path.join(raw_file_path, r"brand_401_num.txt")
    get_brand_num(raw_file_name, result_file_name)
    show_plot(result_file_name)