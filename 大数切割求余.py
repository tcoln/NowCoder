import sys
nums = sys.stdin.readline().strip()
l = len(nums)
T = int(sys.stdin.readline().strip())
ais = {}
ans = [0]*T
for i in range(T):
	tmp = int(sys.stdin.readline().strip())
	ais[tmp] = 0
	ans[i] = tmp
for L in range(l):
	yu = 0
	for R in range(L,l):
		num = yu * 10 + int(nums[R])
		yu = num % 1000000007
		if yu in ais:
			ais[yu] += 1
print ais, ans
for i in range(T):
	print ais.get(ans[i],0)
