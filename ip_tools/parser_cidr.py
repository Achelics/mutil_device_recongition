#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

from IPy import IP

ip_cidr = "192.168.12.0/24"

ip_list = IP(ip_cidr)

ip_file = open("ip_list_lan", "w")

for ip in ip_list:
    ip_file.write(str(ip) + "\n")

