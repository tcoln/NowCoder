import sys
n = input()
m = input()
routes = []
for i in range(m):
	line = sys.stdin.readline().strip().split()
	routes.append((int(line[0]), int(line[1]), int(line[2])))
visited = []
global ans
ans = float('inf')
def bp(routes, pre, cost, visits):
	global ans
	if visits == n:
		if pre == 0 and cost < ans:
			ans = cost
		print cost, visited
		return 
	for r in routes:
		des = -1
		if (r[0] == pre and r[1] not in visited):
			des = r[1]
		if (r[1] == pre and r[0] not in visited):
			des = r[0]
		if des != -1:
			visited.append(des)
			bp(routes, des, cost+r[2], visits+1)
			visited.remove(des)
bp(routes, 0, 0, 0)
print ans
