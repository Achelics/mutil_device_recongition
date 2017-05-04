#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

import multiprocessing
import os as _os


def get_ip_file(raw_path, raw_file_name, ip_path):
    result_file_name = raw_file_name.split('.')[0] + '_ip.txt'
    result_file = open(_os.path.join(ip_path, result_file_name), 'a')
    num_count = 0
    with open(_os.path.join(raw_path, raw_file_name), 'r') as f:
        for line in f:
            num_count += 1
            if num_count > 1:
                ip = line.split(',')[0]
                result_file.write(ip + '\n')
    f.close()
    result_file.close()
    print str(raw_file_name) + ' 的个数为：' + str(num_count-1)


if __name__ == '__main__':
    raw_path = "F:\\mutil_result\\five_protocol_50"
    ip_path = "F:\\mutil_result\\five_protocol_50\\ip_dir"

    ftp_csv = "zmap_ftp.csv"
    ssh_csv = "zmap_ssh.csv"
    telnet_csv = "zmap_telnet.csv"
    http_csv = "zmap_http.csv"
    rtsp_csv = "zmap_rtsp.csv"

    p1 = multiprocessing.Process(target=get_ip_file, args=(raw_path, ftp_csv, ip_path))
    p2 = multiprocessing.Process(target=get_ip_file, args=(raw_path, ssh_csv, ip_path))
    p3 = multiprocessing.Process(target=get_ip_file, args=(raw_path, telnet_csv, ip_path))
    p4 = multiprocessing.Process(target=get_ip_file, args=(raw_path, http_csv, ip_path))
    p5 = multiprocessing.Process(target=get_ip_file, args=(raw_path, rtsp_csv, ip_path))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()


