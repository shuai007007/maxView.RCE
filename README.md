# maxView.RCE
一款检测maxView.RCE漏洞的脚本
![图片](https://github.com/user-attachments/assets/7c2b2a46-fded-4b1c-b7f7-b9b1ce4ce205)
```
简介
maxView Storage Manager 是一款企业存储和通信解决方案的管理系统。maxView Storage Manager 存在代码执行漏洞，攻击者可通过dynamiccontent.
properties.xhtml 执行任意代码获取服务器权限。maxView Storage Manager 存在代码执行漏洞，攻击者可通过dynamiccontent.properties.xhtml执
行任意代码获取服务器权限。

使用说明
[+]maxView.py -u --url http://www.xxx.com 即可进行单个漏洞检测
[+]maxView.py -f --file targetUrl.txt 即可对选中文档中的网址进行批量检测
[+]maxView.py -h --help 查看更多详细帮助信息

Fofa
title==“maxView Storage Manager - Login”
```
