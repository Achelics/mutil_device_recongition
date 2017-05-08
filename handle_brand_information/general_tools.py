#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/05'
import json

# 根据字典前两个值进行去重
def remove_2duplicate(dict_list):
    seen = set()
    new_dict_list = []
    for dict in dict_list:
        t_dict = {'Brand': dict['Brand'], 'Model': dict['Model']}
        t_tup = tuple(t_dict.items())
        if t_tup not in seen:
            seen.add(t_tup)
            new_dict_list.append(dict)
    return new_dict_list


# 根据字典前两个值进行去重
def remove_2duplicate_ingoreletter(dict_list):
    new_dict_list = []
    single_brand_model = []
    for raw_dict in dict_list:
        t_dict = {'Brand': str(raw_dict['Brand']).upper(), 'Model': str(raw_dict['Model']).upper()}
        if t_dict not in new_dict_list:
            single_brand_model.append(raw_dict)
        new_dict_list.append(t_dict)
    return single_brand_model


