# IPserch
一个帮助你获取域名背后IP地址的简易Python脚本

## 使用方法

### 脚本简介
本脚本使用Python+dig命令实现获取，如果您使用的是Linux以及macOS，那么可以在安装Python后直接使用，如果是Windows的用户，那么请自行安装dig，或修改脚本中代码使用。
`def`代码块为脚本的本体，每一段代码都有其相对应的注释，可以很方便地查看。    
<br/>
执行脚本建议先进入脚本所在目录并执行
```
python3 ip.py
```
直接用绝对路径执行可能会出现莫名其妙的问题

### 简易使用
您只需要将域名写入一个纯文本文件，并将此文件的相对/绝对路径，以及输出IP用的文件路径写入到`ips("此处填写域名所在文件路径","此处填写输出IP文件路径")`当中即可   
> 例如将使用到相对路径为`list/Apple.list`中的域名转换为相应IP地址并输出到`ip/Apple.list`中（并不需要新建此文件，如果`ip/Apple.list`不存在，那么脚本将会自动创建这个文件）
> 就写成`ips("list/Apple.list","ip/Apple.list")`
当然，如果有多个文件的话，可以不断向脚本中添加`ips(hostlist,IPlist)`     
像这样
```
#!/usr/bin/env python
#coding:utf-8

import os,sys,socket,re

def ips(hostlist,IPlist):
    print("读取域名列表" + hostlist)
    ipserch = os.popen("dig +noall +answer -f " + hostlist)    #使用dig获取ip地址并写入一个临时文件
    print("获取IP中......")

    readip = ipserch.read()
    ipserch.close()

    pattern = re.compile(r"((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    result = pattern.findall(readip)     #提取文件中的IP

    with open(IPlist,'w+') as f:    #将IP写入到文件中
        for line in result:
            f.write('IP-CIDR,' + line + '/24,no-resolve' + '\n')


ips("ipserch/Apple.list","ip/Apple.list")
ips("ipserch/Amazon.list","ip/Amazon.list")
ips("ipserch/Bahamut.list","ip/Bahamut.list")
ips("ipserch/Developer.list","ip/Developer.list")
ips("ipserch/Github.list","ip/Github.list")
ips("ipserch/Google.list","ip/Google.list")
ips("ipserch/Netflix.list","ip/Netflix.list")
ips("ipserch/OneDrive.list","ip/OneDrive.list")
ips("ipserch/GoogleFCM.list","ip/GoogleFCM.list")
ips("ipserch/Pixiv.list","ip/Pixiv.list")
ips("ipserch/Porn.list","ip/Porn.list")
ips("ipserch/YouTube.list","ip/YouTube.list")

print("全部写入完成！")
```

### 进阶使用
#### 修改dig命令
在`def`中，有一句`ipserch = os.popen("dig +noall +answer -f " + hostlist)`，括号中的便是使用到的shell命令，如果有需要，可以自行修改
#### 修改输出
在`def`中，`with`语句下的`for`循环为向`IPlist`所指代的文件中写入IP，如果您没有修改`f.write(line + '\n')`，那么输出的结果会长这样
```
17.142.160.39
17.178.96.39
17.172.224.28
17.254.0.91
67.199.248.13
67.199.248.12
```
你可以自由修改`f.write(line + '\n')`括号中的内容以改变输出结果，比如将其修改成这样`f.write("IP:" + line + '\n')`，输出结果就会变为
```
IP:17.142.160.39
IP:17.178.96.39
IP:17.172.224.28
IP:17.254.0.91
IP:67.199.248.13
IP:67.199.248.12
```
以此类推。