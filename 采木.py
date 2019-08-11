import sys
N = int(sys.stdin.readline().strip())
alltime = 0
tool = 1
for i in range(N):
	time = [int(t) for t in sys.stdin.readline().strip().split(' ')]
	tool2 = 0 if tool == 1 else 1    
	if time[tool] <= time[2] + time[tool2]:
		alltime += time[tool]
	else:
		alltime += time[2] + time[tool2]
		tool = tool2    
	print alltime, tool
print alltime        
