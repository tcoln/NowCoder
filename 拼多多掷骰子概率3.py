import sys
n = input()
nums = [int(i) for i in sys.stdin.readline().strip().split()]
nums.sort()
maxn = nums[-1]
fenmu = 1
for num in nums:
    fenmu *= num
fenzi = 0
for mnum in range(1, maxn+1):
    types = 1
    bigcount = 0
    for num in nums:
        if num < mnum: 
		types *= num
	else:
		bigcount += 1
    types *= mnum**bigcount - (mnum-1)**bigcount
    fenzi += mnum*types
#print fenzi, fenmu
print ('%.2f'%(1.0*fenzi/fenmu))

