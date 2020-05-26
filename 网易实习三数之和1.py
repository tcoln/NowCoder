#coding:utf-8
import sys

def func(s):
    nums = s.split(',')
    ll = len(nums)
    for i in range(ll):
        nums[i] = int(nums[i])
    target = nums[0]
    nums = nums[1:]
    nums.sort()
    ans = 0
    l = len(nums)
    for i in range(l-2):
        newtar = target - nums[i]
        for j in range(i+1, l-1):
            newtar2 = newtar - nums[j]
            for k in range(j+1,l):
                if nums[k] == newtar2:
                    ans += 1
    return ans

line = sys.stdin.readline().strip()
print func(line)

