# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
    	self.s_in = []
	self.s_out = []
    def push(self, node):
        # write code here
        self.s_in.append(node)
    def pop(self):
        # return xx
        while(self.s_in):
            self.s_out.append(self.s_in.pop())
        ans = self.s_out.pop()
        while(self.s_out):
            self.s_in.append(self.s_out.pop())
        return ans

if __name__ == '__main__':
    s = Solution()
    s.push('PSH1')
    s.push('PSH2')
    s.push('PSH3')
    print s.pop()
    print s.pop()
    s.push('PSH4')
    print s.pop()
