import sys
import collections as coll
import heapq
n = input()
T = sys.stdin.readline().strip()
m = input()
ans = 0
lt = len(T)
for mm in range(m):
    s = sys.stdin.readline().strip()
    l = len(s)
    i = j = 0
    while i < lt and T[i] == s[j]:
        i += 1
        j += 1
        if j >= l: j = 0
    if i == lt: ans += 1
    print s, i, lt
print ans
