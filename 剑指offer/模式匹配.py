# -*- coding:utf-8 -*-
# 递归状态机自旋匹配
class Solution:
    def match(self, s, pattern):
        # write code here
        if s == None or pattern == None:
            return False
        l1 = len(s)
        l2 = len(pattern)
        def matchStr(i, j):
            if i == l1 and j == l2:
                return True
            if i != l1 and j == l2:
                return False
            isMatch = False
            if i < l1 and s[i] == pattern[j] or (i < l1 and pattern[j] == '.'):
                isMatch = isMatch or matchStr(i+1, j+1)
            if j+1 < l2 and pattern[j+1] == '*':
                isMatch = matchStr(i, j+2) # * match 0 char
                if not isMatch and i < l1 and (s[i] == pattern[j] or pattern[j] == '.'):
                    isMatch = isMatch or matchStr(i+1, j+2) or matchStr(i+1, j) # * match 1 char or * match 2+ char  
            return isMatch
        return matchStr(0, 0)
