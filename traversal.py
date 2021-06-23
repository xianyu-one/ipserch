#!/usr/bin/env python
#coding:utf-8
#用于遍历文件夹

def document_path(path,extension):    #自动遍历文件夹
    filelist = os.listdir(path)
    for item in filelist:        
        if item.endswith(extension):       #用if语句寻找listpath中定义的文件夹中的.list后缀的文件
            document = path + item
            return document