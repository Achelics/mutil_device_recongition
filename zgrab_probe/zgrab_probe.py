#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/18'

import os as _os
import multiprocessing

def zgrab_http(ip_list_file="", port="80", result_banner="banner80.json", **kwagrs):
    """
        获取http协议标语和首页信息
    :param ip_list_file: ip列表文件
    :param port: 探测的端口
    :param result_banner: 生成标语的结果文件
    :param kwagrs: 其它的参数
    :return:
    """
    if "zmap_file_name" in kwagrs:
        zmap_file_name = kwagrs["zmap_file_name"]
    else:
        zmap_file_name = "zmap_http.csv"
    if "bandwidth" in kwagrs:
        bandwith = kwagrs["bandwidth"]
    else:
        bandwith = "2M"
    cmd = ("zmap -p " + port + " -B " + bandwith + " -w " + ip_list_file
           + " --output-fields=* | ztee " + zmap_file_name +
           " | ./zgrab --port=" + port + " --http=/ --http-max-redirects=2 --http-user-agent='Mozilla/5.0 (Windows NT 10.0; WOW64)' --output-file=" + result_banner)
    _os.system(cmd)


def zgrab_protocol(ip_list_file="", port="", result_banner="banner.json", protocol="", **kwagrs):
    """
        获取通用协议标语信息
    :param ip_list_file: ip列表文件
    :param port: 探测的端口
    :param result_banner: 生成标语的结果文件
    :param protocol: 抓取通用协议标语的名称
    :param kwagrs: 其它的参数
    :return:
    """
    if "zmap_file_name" in kwagrs:
        zmap_file_name = kwagrs["zmap_file_name"]
    else:
        zmap_file_name = "zmap_procotol.csv"
    if "bandwidth" in kwagrs:
        bandwith = kwagrs["bandwidth"]
    else:
        bandwith = "2M"
    cmd = ("zmap -p " + port + " -B " + bandwith + " -w " + ip_list_file
           + " --output-fields=* | ztee " + zmap_file_name +
           " | ./zgrab --port=" + port + " --" + protocol + " --output-file=" + result_banner)
    _os.system(cmd)


def zgrab_proper_protocol(ip_list_file="", port="", result_banner="banner.json",**kwagrs):
    """
            获取专有协议标语信息
        :param ip_list_file: ip列表文件
        :param port: 探测的端口
        :param result_banner: 生成标语的结果文件
        :param kwagrs: 其它的参数
        :return:
        """
    if "zmap_file_name" in kwagrs:
        zmap_file_name = kwagrs["zmap_file_name"]
    else:
        zmap_file_name = "zmap_http.csv"
    if "bandwidth" in kwagrs:
        bandwith = kwagrs["bandwidth"]
    else:
        bandwith = "2M"
    data_file = ""
    if "data_file" in kwagrs:
        data_file = kwagrs["data_file"]

    cmd = ("zmap -p " + port + " -B " + bandwith + " -w " + ip_list_file
           + " --output-fields=* | ztee " + zmap_file_name +
           " | ./zgrab --port=" + port + " --data=" + data_file + " --output-file=" + result_banner)
    _os.system(cmd)


if __name__ == '__main__':

    ip_list_file = "ipList.txt"
    http_kw = dict()
    ftp_kw = dict()
    ssh_kw = dict()
    telnet_kw = dict()
    rtsp_kw = dict()

    http_kw["ip_list_file"] = ip_list_file
    http_kw["port"] = "80"
    http_kw["result_banner"] = "banner80.json"
    http_kw["zmap_file_name"] = "zmap_http.csv"

    ftp_kw["ip_list_file"] = ip_list_file
    ftp_kw["port"] = "21"
    ftp_kw["result_banner"] = "banner21.json"
    ftp_kw["protocol"] = "ftp"
    ftp_kw["zmap_file_name"] = "zmap_ftp.csv"

    ssh_kw["ip_list_file"] = ip_list_file
    ssh_kw["port"] = "22"
    ssh_kw["result_banner"] = "banner22.json"
    ssh_kw["protocol"] = "ssh"
    ssh_kw["zmap_file_name"] = "zmap_ssh.csv"

    telnet_kw["ip_list_file"] = ip_list_file
    telnet_kw["port"] = "23"
    telnet_kw["result_banner"] = "banner23.json"
    telnet_kw["protocol"] = "telnet"
    telnet_kw["zmap_file_name"] = "zmap_telnet.csv"

    rtsp_kw["ip_list_file"] = ip_list_file
    rtsp_kw["port"] = "554"
    rtsp_kw["result_banner"] = "banner554.json"
    rtsp_kw["data_file"] = "rtsp-req"
    rtsp_kw["zmap_file_name"] = "zmap_rtsp.csv"

    p1 = multiprocessing.Process(target=zgrab_http, kwargs=http_kw)
    p2 = multiprocessing.Process(target=zgrab_protocol, kwargs=ftp_kw)
    p3 = multiprocessing.Process(target=zgrab_protocol, kwargs=ssh_kw)
    p4 = multiprocessing.Process(target=zgrab_protocol, kwargs=telnet_kw)
    p5 = multiprocessing.Process(target=zgrab_proper_protocol, kwargs=rtsp_kw)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

