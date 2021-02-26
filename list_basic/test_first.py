#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 20:25
# @Author  : Joey Jiang
# @Site    : 
# @File    : test_first.py
# @Software: PyCharm


'''
1. 实现一个函数，要求对一个列表里面所有数字求和，

如果里面含有非数字的元素。直接跳过。比如[1,2,3] 输出是6，
如果 是[1,2,4,"a"] 输出是7。 并在另外一个包（目录）里面调用这个函数
'''
import pytest

from list_basic.first import list_sum_only_with_number


@pytest.mark.parametrize("input_value,equal", [
    ([], 0),
    (["a"], 0),
    ([1, 2, 3, "a"], 6),
    ([1, 2, 4], 7)]
                         )
def test_frist(input_value, equal):
    sum = list_sum_only_with_number(input_value)
    assert sum == equal
