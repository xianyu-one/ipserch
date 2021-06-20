#!/usr/bin/env python
#coding:utf-8

import os,sys,socket,re

def ips(hostlist,IPlist):
    print("读取域名列表" + hostlist)
    ipserch = os.popen("dig +noall +answer -f " + hostlist)    #使用dig获取ip地址并写入一个临时文件
    print("获取IP中......")

    readip = ipserch.read()    #读取dig命令输出的结果
    ipserch.close()

    pattern = re.compile(r"((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    result = pattern.findall(readip)    #提取IP地址，并储存为一个列表

    with open(IPlist,'w+') as f:    #将列表中的IP地址写入文件
        for line in result:
            f.write(line + '\n')


ips("list/Apple.list","ip/Apple.list")

print("全部写入完成！")