#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 21:13
# @Author  : Joey Jiang
# @Site    : 
# @File    : first.py
# @Software: PyCharm
import os


def first(path):
    '''
    1.查找/tomcat/log目录下的log文件，
    如果文件最后修改时间是在一小时之前，把此文件打包压缩，备份到/home/back/log目录下

    :return:
    '''
    file_list=os.listdir(path)

    for file in file_list:
        os.stat("")