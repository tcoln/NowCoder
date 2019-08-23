count = int(input())
line = [int(i) for i in input().strip().split()]
line = sorted(line)
ansD = {}
for i in line:
	if not i in ansD:
		ansD[i] = 1
	else:
		ansD[i+i]= 1
		del ansD[i]
print (len(ansD))
