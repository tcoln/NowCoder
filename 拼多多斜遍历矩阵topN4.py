import sys
line = sys.stdin.readline().strip().split()
n, m, k = int(line[0]), int(line[1]), int(line[2])
if n > m: m, n = n, m
nn = [n-1]*m + range(n-2, -1, -1)
mm = range(m-1, -1, -1) + [0]*(n-1)
ll = range(1,n) + [n]*(m+1-n)+ range(n-1, 0, -1)
starts = len(nn)
for start in range(starts):
    starti = nn[start]
    startj = mm[start]
    l = ll[start]
    if k > l: 
	k -= l
    else:
    	nums = []
	while l > 0:
       		num = (starti+1)*(startj+1)
		nums.append(num)
		starti -= 1
		startj += 1
		l -= 1
	nums.sort(reverse=True)
	print nums[k-1]
	break	
