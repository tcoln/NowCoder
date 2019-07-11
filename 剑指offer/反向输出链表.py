# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ans = []
        tmp = []
        cur = listNode
        while(cur):
            tmp.append(cur.val)
	    cur = cur.next
        while(tmp):
            ans.append(tmp.pop())
        return ans

if __name__ == '__main__':
    s = Solution()
    h = ListNode(3)
    h.next = ListNode(2)
    h.next.next = ListNode(1)
    print s.printListFromTailToHead(h)
