# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        ans = []
        def preOrder(r, path, pSum):
            if r:
                pSum += r.val
                newPath = list(path)
                newPath.append(r.val)
                # 判断是叶节点
                if r.left == None and r.right == None:
                    if pSum == expectNumber:
                        ans.append(newPath)
                preOrder(r.left, newPath, pSum)
                preOrder(r.right, newPath, pSum)

        preOrder(root, [], 0)
        return ans
