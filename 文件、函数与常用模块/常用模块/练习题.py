#1. logging模块有几个日志级别？
#答：logging 共有五个日志级别，DEBUG,INFO,WARNING,ERROR,CRITCAL

# 请配置logging模块，使其在屏幕和文件里同时打印以下格式的日志
# 2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts
# import logging
# # 屏幕
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# #文件
# fh = logging.FileHandler('mysql.log')
# # 输出格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s- %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
#
# logger = logging.getLogger("mysql")
# logger.setLevel(logging.DEBUG)
#
# logger.addHandler(ch)# 将输出到屏幕绑定到logger
# logger.addHandler(fh)# 将输出到文件绑定到logger
#
# logger.error('too many login attempts')
#3.json、pickle、shelve三个区别是什么？
# 1. json跨语言，体积小，用于网络传输
# 2. pickle只支持python，不能跨语言，支持python所有数据类型
# 3. shelve支持多行dumps
#4. json的作用的是什么
# 答：json的作用是将内存中的数据类型以文件类型保存到本地，或者保存到网络，下次使用时只需要读取json文件中的数据会自动转换成数据类型
#5. subprocess执行命令方法有几种？
# 答：三种。run(),call(),Popen()
#6. 为什么要设计好目录结构？
#  答：软件开发的文件规范，提高软件的可扩展，可阅读性
#5. 代码如下：
"""
'''
Linux当前目录/usr/local/nginx/html/
文件名：index.html
'''
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(index.html)))
print(BASE_DIR)
"""
#1. 打印的内容是什么？
#2.os.path.dirname和os.path.abspath含义是什么？
# 答：os.path.dirname的含义是返回上一级,os.path.abspath的含义是获得绝对路径

#  6.通过configparser模块完成以下功能
"""文件名my.cnf

[DEFAULT]

[client]
port = 3306
socket = /data/mysql_3306/mysql.sock

[mysqld]
explicit_defaults_for_timestamp = true
port = 3306
socket = /data/mysql_3306/mysql.sock
back_log = 80
basedir = /usr/local/mysql
tmpdir = /tmp
datadir = /data/mysql_3306
default-time-zone = '+8:00'

1.修改时区 default-time-zone = '+8:00' 为 校准的全球时间 +00:00
2.删除 explicit_defaults_for_timestamp = true
3.为DEFAULT增加一条 character-set-server = utf8
"""
# 答案：/usr/local/bin/python3.7 /Users/wualin/Documents/python学习笔记/文件、函数与常用模块/常用模块/day5/conf.py

# 10.写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母
# import string
# import random
# s = ''.join(random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,6))
# print(s)
# 11. 利用正则表达式提取到 luffycity.com ，内容如下
"""
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>luffycity.com</title>
</head>
<body>
</body>
</html>
"""
# import re
# f = open("html.html",'r',encoding="utf-8")
# data = f.read()
# s = re.search('luffycity.com',data)
# print(s.group())

# 12.写一个用户登录验证程序，文件如下
# {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
#  答案：/usr/local/bin/python3.7 /Users/wualin/Documents/python学习笔记/文件、函数与常用模块/常用模块/day6/j.py

"""
最近luffy买了个tesla，通过转账的形式，并且支付了5%的手续费，tesla价格为75万。文件为json，请用程序实现该转账行为。
需求如下：

目录结构为
.
├── account
│   ├── luffy.json
│   └── tesla.json
└── bin
      └── start.py
当执行start.py时，出现交互窗口

   ------- Luffy Bank ---------
  1.  账户信息
  2.  转账
选择1 账户信息 显示luffy的当前账户余额。
选择2 转账 直接扣掉75万和利息费用并且tesla账户增加75万
"""
