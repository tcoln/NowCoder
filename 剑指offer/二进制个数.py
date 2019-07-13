# -*- coding:utf-8 -*-
# write code here
n = int(raw_input())
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        
        #return sum([(n>>i & 1) for i in range(0,32)])
        
        ans = 0
        if n < 0:
            n = n&0xffffffff
        while(n):
            ans += 1
            n = n&(n-1)
        return ans
