#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''
import json
if __name__ == '__main__':
    file_name = r"F:\mutil_result\401_brand_analysis\match_401.json"
    result_file = open(r"include_string_brand.json", "a")
    with open(file_name, "r") as f:
        for line in f:
            raw_data = json.dumps(line.strip("\n"), encoding="UTF-8", ensure_ascii=False)
            new_line = eval(json.loads(raw_data))
            output = new_line["Output"]
            if output:
                result_file.write(line)
    f.close()
    result_file.close()