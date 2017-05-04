#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''

import subprocess as _subprocess


def run_cmd(cmd, filename):
    result_file = open(filename, 'a')
    zproc = _subprocess.Popen(args=cmd,
                             stdout=_subprocess.PIPE,
                             stderr=_subprocess.PIPE,
                             universal_newlines=True,
                             shell=True,
                             bufsize=0)
    try:
        while zproc.poll() is None:
            for streamline in iter(zproc.stdout.readline, ''):
                result_file.write(streamline)
                print streamline
        result_file.close()
    except KeyboardInterrupt:
        print("keyboard interruption, stopping zmap.... ")
        exit()


if __name__ == '__main__':
    cmd = "python D:\Users\Achelics\PycharmProjects\mutil_device_recongition\count_alive_ip\count_ip.py"
    file_name = "F:\\mutil_result\\five_protocol_50\\ip_marked_result.txt"
    run_cmd(cmd, file_name)