import sys
N = 5 #input()
trees = [i for i in range(101)]
removes = [9, 15, 27, 35, 6] #[int(i) for i in sys.stdin.readline().strip().split()]
for i in removes:
	trees[i] = -1
print trees
maxI = maxL = 0
for i in range(1, 101):
	tmpL = 0
	for j in range(i, 101, 2):
		if trees[j] != -1:
			tmpL += 1
		else:
			break
	if tmpL > maxL: 
		maxI = i
		maxL = tmpL
print maxI, maxL
