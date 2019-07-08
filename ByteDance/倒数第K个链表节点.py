#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

class ListNode(object):
    def __init__(self, v):
        self.v = v
        self.next = None
        
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        v = int(sys.stdin.readline().strip())
        if i == 0:
            head = ListNode(v)
            pre = head
        else:
            cur = ListNode(v)
            pre.next = cur
            pre = cur
    k = int(sys.stdin.readline().strip())
    if k >= n:
	print None
    else:
	ans = cur = head
    	i = 0
    	while(cur.next):
        	cur = cur.next
        	i += 1
        	if i > k:
            		ans = ans.next
			print ans.v, cur.v
    	print ans.v
