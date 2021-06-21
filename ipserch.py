#!/usr/bin/env python
#coding:utf-8

import os,re

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

def dicide(listpath_original,ippath_original,extension_original):   #判断输入的路径
    if listpath_original.endswith('/'):    #确定域名列表文件所在文件夹路径是否带有‘/’结尾
        if ippath_original.endswith('/'):    #确定IP列表的文件夹路径是否带有‘/’结尾
            listpath = listpath_original
            ippath = ippath_original
            if extension_original.startswith('.'):
                extension = extension_original
            else:
                extension = '.' + extension_original
            list_ip_path(listpath,ippath,extension)
        else:
            ippath = ippath_original + '/'
            listpath = listpath_original
            if extension_original.startswith('.'):
                extension = extension_original
            else:
                extension = '.' + extension_original
            list_ip_path(listpath,ippath,extension)
    else:
        listpath = listpath_original + '/'
        if ippath_original.endswith('/'):
            ippath = ippath_original
            if extension_original.startswith('.'):
                extension = extension_original
            else:
                extension = '.' + extension_original
            list_ip_path(listpath,ippath,extension)
        else:
            ippath = ippath_original + '/'
            if extension_original.startswith('.'):
                extension = extension_original
            else:
                extension = '.' + extension_original
            list_ip_path(listpath,ippath,extension)

listpath_original = input('请输入域名列表文件所在文件夹路径：')
ippath_original = input('请输入输出IP列表的文件夹路径：')
extension_original = input('请输入储存域名的文件的后缀：')
dicide(listpath_original,ippath_original,extension_original)

print("全部写入完成！")
