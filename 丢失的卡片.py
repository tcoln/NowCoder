import sys
nums = [int(num) for num in sys.stdin.readline().strip().split(' ')]
N = 200
flag = 0
for n in range(1, N+1):
	allnums = [0 for _ in range(10)]
	for num in range(1, n+1):
		i = num
		while i > 0:
			yu = i % 10
			i /= 10
			allnums[yu] += 1
	for x in range(1, n+1):
		tmp = list(allnums)
		i = x
		while i > 0:
			yu = i % 10
			i /= 10
			tmp[yu] -= 1
		if tmp == nums:
			flag = 1
			print str(n) + ' ' + str(x)
if not flag:
	print 'NO ANSWER'
