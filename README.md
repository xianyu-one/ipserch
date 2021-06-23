# IPserch
一个帮助你获取域名背后IP地址的简易Python脚本

## 使用方法

本脚本使用Python+dig命令实现获取，如果您使用的是Linux以及macOS，那么可以在安装Python后直接使用，如果是Windows的用户，那么请自行安装dig，或修改脚本中代码使用。
`def`代码块为脚本的本体，每一段代码都有其相对应的注释，可以很方便地查看。    
<br/>
执行脚本建议先进入脚本所在目录并执行
```
python3 ipserch_All_in_One.py
```
或执行以下代码使用将代码段分离的版本（目前分体式的脚本包含`ipserch.py`、`dicide.py`两个文件,请保正两个文件在同一文件夹下）
```
python3 ipserch.py
```
直接用绝对路径执行可能会出现莫名其妙的问题

<br/>
如果您并没有安装Python，同时使用的是Mac的话可以下载打包好的可执行文件`ipserch`直接使用（但运行效率会比较差）