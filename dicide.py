#!/usr/bin/env python
#coding:utf-8
#用于检测并修正数据输入格式的库

def dicide_path(path):    #用于检测输入路径是否带有/
    path_back = ''
    if path.endswith('/'):
        path_back = path
        return path_back
    else:
        path_back = path + '/'
        return path_back

def dicide_extension(extension):   #用于检测输入文件后缀是否带有.
    extension_back = ''
    if extension.startswith('.'):
        extension_back = extension
        return extension_back
    else:
        extension_back = '.' + extension
        return extension_back