import sys
import collections as coll
import heapq
line = sys.stdin.readline().strip().split()
t = int(line[0])
k = int(line[0])
fs = [1]*(10000+1)
for tt in range(t):
    line = sys.stdin.readline().strip().split()
    a = int(line[0])
    b = int(line[1])
    ans = 0
    for i in range(1, b+1):
	if i >= k-1:
		fs[i] = fs[i-1]+fs[i-2]
	if i >= a:
		ans += fs[i]
    	#print fs[:i+1], i, ans
    print ans
