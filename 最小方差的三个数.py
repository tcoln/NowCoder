import sys
N = int(sys.stdin.readline().strip())
global ans
ans = float('inf')
nums = [int(i) for i in sys.stdin.readline().strip().split(' ')]
nums.sort()
l = len(nums)
for i in range(l-2):
    path = nums[i:i+3]
    ave = sum(path)/3.0
    squ = [(p-ave)**2 for p in path]
    var = sum(squ)/3.0
    if var < ans:
        ans = var
print '%.2f'%(ans)
