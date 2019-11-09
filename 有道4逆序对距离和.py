import sys
n = input()
nums = [int(num) for num in sys.stdin.readline().strip().split()]
ret = 0
for i in range(1, n):
        for j in range(i-1, -1, -1):
            if nums[i] < nums[j]:
                ret += i - j
print ret
