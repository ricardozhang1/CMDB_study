#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 17:11
# @Author  : ZhangChaowei
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

import os

# 远端接受数据的服务器
Params = {
    "server": "192.168.184.1",
    "port": 8000,
    "url": "/assets/report/",
    "request_timeout": 30,
}

# 日志文件配置
PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmd.log')




