import sys
import bisect as bi
N = 9 #input()
stones = [1,2,3,4,9,5,6,7,8] #[int(i) for i in sys.stdin.readline().strip().split()]
maxL = [1 for i in range(N)]
preLs = {stones[0]:1}
for i in range(1, N):
	preL = 0
	for j in range(stones[i]-1, 0, -1):
		value = preLs.get(j, -1)
		if value > preL:
			preL = value + 1
	if preL > maxL[i]: 
		maxL[i] = preL
		preLs[stones[i]] = maxL[i]
print N-max(maxL)
