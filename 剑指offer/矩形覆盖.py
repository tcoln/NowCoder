# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        ans = [1 for i in range(number)]
        ans[1] = 2
        for i in range(2, number):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[number-1]
