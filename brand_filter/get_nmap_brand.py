#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = ''
__date__ = ''
import string
import nltk

def brand_remove_stop_word(stop_word_name, raw_file_name, result_file_name):
    stop_word_set = set()
    raw_brand_set = set()
    with open(stop_word_name, 'r') as f:
        for line in f:
            stop_word = line.strip('\n')
            stop_word_set.add(stop_word)
    f.close()

    with open(raw_file_name, 'r') as f_raw:
        for line in f_raw:
            raw_brand = line.strip('\n')
            # 去除停用词
            raw_brand = ' '.join([word for word in raw_brand.split() if word not in stop_word_set])
            # 去除标点符号
            raw_brand = raw_brand.translate(None, string.punctuation)
            # 去除词中小于3的字符串
            raw_brand = ' '.join([word for word in raw_brand.split() if len(word) >= 3])
            raw_brand_set.add(raw_brand)
    f_raw.close()

    result_file = open(result_file_name, 'a')
    for brand in raw_brand_set:
        result_file.write(brand + '\n')
    result_file.close()


def get_namp_raw_vendor():
    brand_set = set()
    source_name = r'/home/achelics/work/data_analysis/mutil_device_recongition/brand_filter/nmap-mac-prefixes'
    result_name = r'/home/achelics/work/data_analysis/mutil_device_recongition/brand_filter/nmap-brand.txt'

    with open(source_name, 'r') as f:
        for line in f:
            if '#' in line:
                continue
            data = str(line.strip('\n'))
            brand = data[6:]
            brand_set.add(brand)
    f.close()

    result_file = open(result_name, 'a')
    for brand in brand_set:
        result_file.write(brand + '\n')
    result_file.close()


if __name__ == '__main__':
    # stop_word_name = r'stop_word.txt'
    # raw_file_name = r'nmap-brand.txt'
    # result_file_name = r'namp_brand_clear.txt'
    # brand_remove_stop_word(stop_word_name, raw_file_name, result_file_name)
    text = nltk.word_tokenize("Sichuan Jiuzhou Electronic Technology")
    word_list = nltk.pos_tag(text)
    print word_list
