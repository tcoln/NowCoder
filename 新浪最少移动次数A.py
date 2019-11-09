#coding=utf-8
import sys
import collections
a = sys.stdin.readline().strip().split(",")
nums = [int(x) for x in a]
l = len(nums)
ans = 0
count = collections.Counter(nums)
if len(count) == l:
    print 0
else:
    nums.sort()
    # 1 1 1 2 3
    for i in range(1, l):
        while nums[i] in nums[:i]:
            nums[i] += 1
            ans += 1
    print ans

