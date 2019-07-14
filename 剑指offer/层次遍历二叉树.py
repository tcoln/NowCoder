# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        que = deque()
	que.append(root)
        while(len(que)):
            pop = que.popleft()
            if pop:
                print pop.val
                que.append(pop.left)
                que.append(pop.right)

s = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
s.PrintFromTopToBottom(r)
