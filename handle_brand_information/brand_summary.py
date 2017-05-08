#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/05/05'

__BRANDZ_SET = set()

__MONITOR_BRAND = set()
__ROUTER_BRAND = set()


def get_brand_summary():
    monitor = r"F:\mutil_result\final_brand_model\monitor_brand.json"
    router = r"F:\mutil_result\final_brand_model\router_brand.json"

    with open(monitor, "r") as monitor_f:
        for line in monitor_f:
            brand = line.strip("\n")
            __BRANDZ_SET.add(brand)
            __MONITOR_BRAND.add(str(brand).upper())
    monitor_f.close()

    with open(router, "r") as router_f:
        for line in router_f:
            brand = line.strip("\n")
            __BRANDZ_SET.add(brand)
            __ROUTER_BRAND.add(str(brand).upper())
    router_f.close()

    brand_seen = set()
    result_file_name = r"F:\mutil_result\final_brand_model\brand.json"
    result_file = open(result_file_name, "a")
    for brand in __BRANDZ_SET:
        if str(brand).upper() not in brand_seen:
            device_type = ""
            if str(brand).upper() in __MONITOR_BRAND:
                device_type = "Monitor" + ","
            if str(brand).upper() in __ROUTER_BRAND:
                device_type += "Router"
            result_file.write(str(brand) + "\t" + device_type)
            result_file.write("\n")
        brand_seen.add(str(brand).upper())
    result_file.close()


if __name__ == '__main__':
    get_brand_summary()
