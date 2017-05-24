#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2017/04/15'

import multiprocessing
import sys
import os as _os
reload(sys)
sys.setdefaultencoding('utf-8')


class CountProtocolIP(multiprocessing.Process):

    def __init__(self, marked_file_name, protocol_marked_file_name, marked_num):
        multiprocessing.Process.__init__(self)
        self.marked_file_name = marked_file_name
        self.protocol_marked_file_name = protocol_marked_file_name
        self.marked_num = marked_num


    def get_num_distribute(self):
        """
            根据标记的ip文件，得到协议开放的统计结果
            :return:
        """
        first_num = 0
        second_num = 0
        third_num = 0
        forth_num = 0
        five_num = 0
        with open(self.protocol_marked_file_name, 'r') as f:
            for line in f:
                data = line.strip('\n')
                protocol_num = data.split(',')[1:6]
                int_num = map(int, protocol_num)
                number_open = sum(int_num)
                if number_open == 1:
                    first_num += 1
                elif number_open == 2:
                    second_num += 1
                elif number_open == 3:
                    third_num += 1
                elif number_open == 4:
                    forth_num += 1
                elif number_open == 5:
                    five_num += 1
        f.close()
        print (self.protocol_marked_file_name + " 开放的1个协议有：" + str(first_num) + " 开放的2个协议有：" + str(second_num) +
               " 开放的3个协议有：" + str(third_num) + " 开放的4个协议有：" + str(forth_num) +
               " 开放的5个协议有：" + str(five_num))

    def __get_single_protocol_marked(self):
        """
        根据已经标记好的Ip文件得到单个协议的ip标记文件
        """
        protocol_marked_file = open(self.protocol_marked_file_name, 'a')
        num_count = 0
        with open(self.marked_file_name, 'r') as f:
            for line in f:
                data = line.strip('\r\n')
                flag = data.split(",")[self.marked_num]
                if flag == "1":
                    num_count += 1
                    protocol_marked_file.write(line)
        f.close()
        print (self.protocol_marked_file_name + "的数量为: " + str(num_count))

    def run(self):
        self.__get_single_protocol_marked()
        self.get_num_distribute()

if __name__ == '__main__':
    ip_path = "F:\\mutil_result\\five_protocol\\ip_dir\\"
    marked_file = "F:\\mutil_result\\five_protocol\\ip_maeked_compare.txt"

    protocol_list = ["zmap_ftp_ip_marked.txt", "zmap_ssh_ip_marked.txt", "zmap_telnet_ip_marked.txt", "zmap_http_ip_marked.txt", "zmap_rtsp_ip_marked.txt"]
    for i in range(len(protocol_list)):
        protocol_marked_name = ip_path + protocol_list[i]
        marked_num = i+1
        protocol_process = CountProtocolIP(marked_file, protocol_marked_name, marked_num)
        protocol_process.start()



