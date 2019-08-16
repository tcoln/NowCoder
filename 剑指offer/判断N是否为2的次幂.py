#coding=utf-8
import sys
def isPow2(n):
    n &= n-1	# O(1)
    return True if n==0 else False

    flag = False	# O(log(n))
    if n % 2 == 1:
        flag = True
    while n:	
        n = n>>1
        if n % 2 == 1:
            if not flag:
                flag = True
            else:
                return False
    return True
for i in range(1, 100):
    print i, isPow2(i)
    

#110 101 = 100 3
#100 011 = 000 7+1/2=n
