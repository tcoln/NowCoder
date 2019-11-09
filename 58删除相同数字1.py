import sys
nums = [int(num) for num in '0,0,1,1,1,2,2,3,3,4'.split(',')]
#nums = [int(num) for num in sys.stdin.readline().strip().split(',')]
l = len(nums)
i = 1
pre = nums[0]
while i < l:
    print  pre, nums[i], nums
    if nums[i] == pre:
        del nums[i]
        i -= 1
	l -= 1
    else:
	pre = nums[i]
    i += 1
print len(nums)
