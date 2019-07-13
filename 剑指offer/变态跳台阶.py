# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 2:
            return number
        jump = [1 for i in range(number)]
        jump[1] = 2
        sumJ = [1 for i in range(number)]
        sumJ[1] = sumJ[0] + jump[1]
        for i in range(2, number):
            jump[i] = sumJ[i-1] + 1
            sumJ[i] = sumJ[i-1] + jump[i] # 为下一次jump计算做准备
        return jump[number-1]
