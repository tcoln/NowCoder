# -*- coding:utf-8 -*-
# 从左下角或者右上角开始遍历，要么找到，要么上移或者右移
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        if array == None:
            return False
        m = len(array)
        n = len(array[0])
        i, j = m-1, 0
        while(i >= 0 and j < n):
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                i -= 1
            else:
                j += 1
        return False

if __name__ == '__main__':
   s = Solution()
   print s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
