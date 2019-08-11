#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************
    
def  GetResult(K):
	n = 1
	sums = 1 / n
	while sums < K:
		n += 1
		sums += float(1)/n
	return n

#******************************结束写代码******************************
_K = int(raw_input())
res = GetResult(_K)
print res 
