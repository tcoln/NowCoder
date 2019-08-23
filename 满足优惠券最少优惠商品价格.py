import sys
line = sys.stdin.readline().strip().split()
X = int(line[0])
N = int(line[1])
items = []
for i in range(N):
	items.append(int(line[2+i]))
items.sort()
global ret
ret = float('inf')
def backtrack(depth, candi, prep, sump):
	global ret
	if sump >= X and sump < ret:
		ret = sump
		return
	for can in candi:
		if can > prep:
			newcan = list(candi)
			newcan.remove(can)
			backtrack(depth+1, newcan, can, sump+can)
backtrack(0, items, -1, 0)
if ret > 3*X: ret = -1
print ret
