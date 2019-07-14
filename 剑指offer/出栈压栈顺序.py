# -*- coding:utf-8 -*-
# 每个出栈的元素不能小于前一个出栈元素位置-1
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        l = len(popV)
        prePos = 1
        for i in range(l):
            if popV[i] not in pushV:
                return False
            pos = pushV.index(popV[i])
            if pos >= prePos - 1:
                pushV.remove(popV[i])
                prePos = pos
            else:
                return False
        return True            
