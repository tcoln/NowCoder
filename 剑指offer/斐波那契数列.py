# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        f = [0 for i in range(40)]
        # 0 1 1 2
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        print f
        return f[n]

if __name__ == "__main__":
	s = Solution().Fibonacci(30)
