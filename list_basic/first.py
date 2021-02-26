#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 20:15
# @Author  : Joey Jiang
# @Site    : 
# @File    : first.py
# @Software: PyCharm

def list_sum_only_with_number(array: list):
    '''
    1. 实现一个函数，要求对一个列表里面所有数字求和，

    如果里面含有非数字的元素。直接跳过。比如[1,2,3] 输出是6，
    如果 是[1,2,4,"a"] 输出是7。 并在另外一个包（目录）里面调用这个函数

    :param array: 列表
    :return: 列表中所有数字相加的和
    '''
    sum = 0
    for i in array:
        if isinstance(i, int):
            sum += i
    return sum
