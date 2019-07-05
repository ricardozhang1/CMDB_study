#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 15:06
# @Author  : ZhangChaowei
# @Site    : 
# @File    : main.py
# @Software: PyCharm

"""
可以把客户端信息收集脚本做成windows和linux两个不同的版本
"""

import os
import sys

# 设置工作目录，使得包和模块能够正常导入
BASE_DIR = os.path.dirname(os.getcwd())
sys.path.append(BASE_DIR)

from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)  # 传入当前路径







