#!/usr/bin/env python
#coding:utf-8

import os,re,dicide

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

def list_ip_path(listpath,ippath,extension):    #自动遍历文件夹
    filelist = os.listdir(listpath)
    for item in filelist:        
        if item.endswith(extension):       #用if语句寻找listpath中定义的文件夹中的.list后缀的文件
            hostlist = listpath + item
            IPlist = ippath + item
            ips(hostlist,IPlist)

def body(listpath_original,ippath_original,extension_original):
    extension = dicide.dicide_extension(extension_original)    #格式化输入的文件后缀
    listpath = dicide.dicide_path(listpath_original)    #格式化输入的域名列表文件夹路径
    ippath = dicide.dicide_path(ippath_original)    #格式化输入的IP列表路径
    list_ip_path(listpath,ippath,extension)

listpath_original = input('请输入域名列表文件所在文件夹路径：')
ippath_original = input('请输入输出IP列表的文件夹路径：')
extension_original = input('请输入储存域名的文件的后缀：')
body(listpath_original,ippath_original,extension_original)

print("全部写入完成！")