#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

if __name__ == '__main__':
    ftp_set = set()
    ssh_set = set()
    telnet_set = set()
    http_set = set()
    rtsp_set = set()

    with open(r'F:\mutil_result\five_protocol_50\ip_21.txt', 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            ftp_set.add(ip)
    f.close()
    print 'ftp加载完成'

    with open(r'F:\mutil_result\five_protocol_50\ip_22.txt', 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            ssh_set.add(ip)
    f.close()
    print 'ssh加载完成'

    with open(r'F:\mutil_result\five_protocol_50\ip_23.txt', 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            telnet_set.add(ip)
    f.close()
    print 'telnet加载完成'

    with open(r'F:\mutil_result\five_protocol_50\ip_80.txt', 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            http_set.add(ip)
    f.close()
    print 'http加载完成'

    with open(r'F:\mutil_result\five_protocol_50\ip_554.txt', 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            rtsp_set.add(ip)
    f.close()
    print 'rtsp加载完成'

    marked_file = open(r'F:\mutil_result\five_protocol_50\ip_maeked_compare.txt', 'a')
    with open(r'F:\mutil_result\five_protocol_50\ip_result.txt', 'r') as f:
        for line in f:
            ip = line.strip('\r\n')
            result_marked = ip + ','

            if ip in ftp_set:
                result_marked = result_marked + '1' + ','
            else:
                result_marked = result_marked + '0' + ','

            if ip in ssh_set:
                result_marked = result_marked + '1' + ','
            else:
                result_marked = result_marked + '0' + ','

            if ip in telnet_set:
                result_marked = result_marked + '1' + ','
            else:
                result_marked = result_marked + '0' + ','

            if ip in http_set:
                result_marked = result_marked + '1' + ','
            else:
                result_marked = result_marked + '0' + ','

            if ip in rtsp_set:
                result_marked = result_marked + '1'
            else:
                result_marked = result_marked + '0'
            # print result_marked
            marked_file.write(result_marked + '\n')
    f.close()
    marked_file.close()

    print "ip文件标记结束"


