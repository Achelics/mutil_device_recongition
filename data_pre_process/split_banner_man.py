#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/19'

import os as _os
import json as _json
import multiprocessing
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def split_protocol_banner(protocol_validity_json, raw_file_path, raw_file_name, result_path):
    """
        分割原始文件，将个协议标语文件按照ok和error进行分割
    :param protocol_validity_json: 协议过滤json的方法
    :param raw_file_path: 原始json文件所在路径
    :param raw_file_name: 原始文件名称
    :param result_path: 结果文件所在路径
    :return:
    """
    string_file_name = raw_file_name.split(".")[0] + "_stringok.txt"
    ok_file_name = raw_file_name.split(".")[0] + "_ok.json"
    error_file_name = raw_file_name.split(".")[0] + "_error.json"

    string_file = open(_os.path.join(result_path, string_file_name), "a")
    ok_file = open(_os.path.join(result_path, ok_file_name), "a")
    error_file = open(_os.path.join(result_path, error_file_name), "a")

    with open(_os.path.join(raw_file_path, raw_file_name), "r") as f:
        for line in f:
            raw_data = _json.loads(line.strip('\n'), strict=False)
            result = protocol_validity_json(raw_data)
            if result:
                if result["banner_flag"]:
                    string_file.write(_json.dumps(result["banner_string"], encoding="UTF-8", ensure_ascii=False) + "\n")
                    ok_file.write(_json.dumps(result["banner_ok"], encoding="UTF-8", ensure_ascii=False) + "\n")
                else:
                    error_file.write(_json.dumps(result["banner_error"], encoding="UTF-8", ensure_ascii=False) + "\n")
    f.close()
    string_file.close()
    ok_file.close()
    error_file.close()


def ftp_validity_json(raw_data):
    """
        根据原始的banner信息，返回一个字典类型
    :param raw_data: 原始的banner的json信息
    :return: result： 字典类型
                "banner_string": banner字符串信息
                "banner_ok": 返回为ok的banner的json信息
                "banner_error": 返回为error的json信息
    """
    result = dict()
    result["banner_flag"] = False
    result["banner_error"] = raw_data
    if "data" in raw_data:
        if "ftp" in raw_data["data"]:
            ftp = raw_data["data"]["ftp"]
            if "banner" in ftp:
                ftp_banner = dict()
                ftp_banner["raw_banner"] = ftp["banner"]
                result["banner_string"] = ftp_banner
                result["banner_ok"] = raw_data
                result["banner_flag"] = True
    return result


def ssh_validity_json(raw_data):
    """
        根据原始的banner信息，返回一个字典类型
    :param raw_data: 原始的banner的json信息
    :return: result： 字典类型
                "banner_string": banner字符串信息
                "banner_ok": 返回为ok的banner的json信息
                "banner_error": 返回为error的json信息
    """
    result = dict()
    result["banner_flag"] = False
    result["banner_error"] = raw_data
    if "data" in raw_data:
        if "ssh" in raw_data["data"]:
            if "server_protocol" in raw_data["data"]["ssh"]:
                if "raw_banner" in raw_data["data"]["ssh"]["server_protocol"]:
                    ssh_banner = dict()
                    ssh_banner["raw_banner"] = raw_data["data"]["ssh"]["server_protocol"]["raw_banner"]
                    result["banner_string"] = ssh_banner
                    result["banner_ok"] = raw_data
                    result["banner_flag"] = True
    return result


def telnet_validity_json(raw_data):
    """
        根据原始的banner信息，返回一个字典类型
    :param raw_data: 原始的banner的json信息
    :return: result： 字典类型
                "banner_string": banner字符串信息
                "banner_ok": 返回为ok的banner的json信息
                "banner_error": 返回为error的json信息
    """
    result = dict()
    result["banner_flag"] = False
    result["banner_error"] = raw_data
    if "data" in raw_data:
        if "telnet" in raw_data["data"]:
            if "banner" in raw_data["data"]["telnet"]:
                telnet_banner = dict()
                telnet_banner["raw_banner"] = raw_data["data"]["telnet"]["banner"]
                result["banner_string"] = telnet_banner
                result["banner_ok"] = raw_data
                result["banner_flag"] = True
    return result


def rtsp_validity_json(raw_data):
    """
        根据原始的banner信息，返回一个字典类型
    :param raw_data: 原始的banner的json信息
    :return: result： 字典类型
                "banner_string": banner字符串信息
                "banner_ok": 返回为ok的banner的json信息
                "banner_error": 返回为error的json信息
    """
    result = dict()
    result["banner_flag"] = False
    result["banner_error"] = raw_data
    if "data" in raw_data:
        if "read" in raw_data["data"]:
            rtsp_banner = dict()
            rtsp_banner["raw_banner"] = raw_data["data"]["read"]
            result["banner_string"] = rtsp_banner
            result["banner_ok"] = raw_data
            result["banner_flag"] = True

    return result


def split_http_web(status_code, raw_file_path="", raw_file_name="", result_path=""):
    """
        根据http协议的状态码得到分割结果
    :param raw_file_path: 原始文件所在路径
    :param raw_file_name: 原始文件名称
    :param result_path: 结果文件路径
    :param status_code: 状态码
    :return:
    """
    status_file_name = raw_file_name.split(".")[0] + "_" + str(status_code) + ".json"
    status_file = open(_os.path.join(result_path, status_file_name), "a")
    with open(_os.path.join(raw_file_path, raw_file_name), "r") as f:
        for line in f:
            raw_data = _json.loads(line.strip('\n'))
            if "data" in raw_data:
                if "http" in raw_data["data"]:
                    if "response" in raw_data["data"]["http"]:
                        response = raw_data["data"]["http"]["response"]
                        if "status_code" in response:
                            code = response["status_code"]
                            if status_code == code:
                                status_file.write(line)
    f.close()
    status_file.close()


if __name__ == '__main__':
    raw_file_path = "F:\\mutil_result\\five_protocol_50"
    result_file_path = "F:\\mutil_result\\five_protocol_50\\data_process"
    # protocol_name_list = ["banner21.json", "banner22.json", "banner23.json", "banner554.json"]
    # protocol_json_list = [ftp_validity_json, ssh_validity_json, telnet_validity_json, rtsp_validity_json]
    # pool = multiprocessing.Pool(processes=4)

    # for i in range(4):
    #     pool.apply_async(split_protocol_banner, args=(protocol_json_list[i], raw_file_path,
    #                                                   protocol_name_list[i], result_file_path))
    http_kw = dict()
    http_kw["raw_file_path"] = raw_file_path
    http_kw["raw_file_name"] = "banner80.json"
    http_kw["result_path"] = result_file_path

    status_code_301 = 403

    http_p_301 = multiprocessing.Process(target=split_http_web, args=(status_code_301,), kwargs=http_kw)

    http_p_301.start()
    http_p_301.join()

    # pool.close()
    # pool.join()




