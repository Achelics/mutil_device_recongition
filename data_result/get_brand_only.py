#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

import os as _os
import json as _json


def get_brand():
    brand_set = set()
    brand_path = r"F:\mutil_result\brand_file"
    cleancss_default_router = _os.path.join(brand_path, "cleancss_default_router.json")
    with open(cleancss_default_router, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"]
            brand_set.add(brand)
    f.close()

    defaultpassword = _os.path.join(brand_path, "defaultpassword.json")
    with open(defaultpassword, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            if eval_raw_data["Product"]:
                brand = eval_raw_data["Product"][0]
                if brand:
                    brand_set.add(brand)
                else:
                    Manufactor = eval_raw_data["Manufactor"][0]
                    brand_set.add(Manufactor)
            else:
                Manufactor = eval_raw_data["Manufactor"][0]
                brand_set.add(Manufactor)
    f.close()

    geniusvision_branddetail = _os.path.join(brand_path, "geniusvision_branddetail.json")
    with open(geniusvision_branddetail, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"][0]
            brand_set.add(brand)
    f.close()

    ipvm_modellist = _os.path.join(brand_path, "ipvm_modellist.json")
    with open(ipvm_modellist, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"][0]
            brand_set.add(brand)
    f.close()

    model_1 = _os.path.join(brand_path, "model_1.json")
    with open(model_1, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"]
            brand_set.add(brand)
    f.close()

    model_2 = _os.path.join(brand_path, "model_2.json")
    with open(model_2, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"]
            brand_set.add(brand)
    f.close()

    portforward = _os.path.join(brand_path, "portforward.json")
    with open(portforward, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"]
            brand_set.add(brand)
    f.close()

    Routermodel_1 = _os.path.join(brand_path, "Routermodel_1.json")
    with open(Routermodel_1, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"]
            brand_set.add(brand)
    f.close()

    Routermodel_2 = _os.path.join(brand_path, "Routermodel_2.json")
    with open(Routermodel_2, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Brand"]
            brand_set.add(brand)
    f.close()

    soleratec_rtsplist = _os.path.join(brand_path, "soleratec_rtsplist.json")
    with open(soleratec_rtsplist, "r") as f:
        for line in f:
            raw_data = _json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            eval_raw_data = eval(_json.loads(raw_data))
            brand = eval_raw_data["Company"][0]
            brand_set.add(brand)
    f.close()

    brand_result_name = _os.path.join(brand_path, "brand_list.json")
    brand_result_file = open(brand_result_name, "a")
    for brand in brand_set:
        brand_result_file.write(brand + "\n")
    brand_result_file.close()

if __name__ == '__main__':
    get_brand()