# -*- coding:utf-8 -*-
from copy import deepcopy

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
	stack1 = [pRoot]
        stack2 = []
        row = 1
        ans = []
        rowAns = []
        while(len(stack1) > 0 or len(stack2) > 0):
            if row % 2 == 1:
                r = stack1.pop()
                if r.left != None:
                    stack2.append(r.left)
                if r.right != None:
                    stack2.append(r.right)
                rowAns.append(r.val)
                if len(stack1) == 0:
                    row += 1
                    ans.append(rowAns)
                    rowAns = []
            else:
                r = stack2.pop()
                if r.right != None:
                    stack1.append(r.right)
                if r.left != None:
                    stack1.append(r.left)
                rowAns.append(r.val)
                if len(stack2) == 0:
                    row += 1
                    ans.append(rowAns)
                    rowAns = []
        return ans

if __name__ == '__main__':
	r = TreeNode(8)
	r.left = TreeNode(6)
	r.right = TreeNode(10)
	r.left.left = TreeNode(5)
	r.left.right = TreeNode(7)
	r.right.left = TreeNode(9)
	r.right.right = TreeNode(11)
	s = Solution()
	print s.Print(r)
