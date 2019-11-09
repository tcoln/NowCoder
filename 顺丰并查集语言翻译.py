import sys
line = sys.stdin.readline().strip().split()
n = int(line[0])
m = int(line[1])
k = int(line[2])
langui = {}
peoples = {}
shazi = set([i for i in range(1, n+1)])
chongfulan = []
for i in range(k):
	line = sys.stdin.readline().strip().split()
	u, v = int(line[0]), int(line[1])
	if u in shazi:
		shazi.discard(u)    
	if not langui.has_key(v):
		langui[v] = [u]
	else:
		langui[v].append(u)
	if u not in peoples:
		peoples[u] = v
	else:
		oldlan = peoples[u]        
		langui[oldlan].extend(langui[v])
		chongfulan.append(v)
if not k:
	print 0
else:
	for lan in chongfulan:
		del langui[lan]    
	print len(langui)-1 + len(shazi)
