import sys
places = 'aabbcddc' #sys.stdin.readline().strip()
l = len(places)
groups = []

def findfromend(a, l, p):
	for i in range(l-1, -1, -1):
		if a[i] == p:
			return i

i = 0
while i < l:
	group = []
	p = places[i]
	group.append(p)
	rindex = findfromend(places, l, p)
	j = i + 1
	while j < rindex+1:
		p = places[j]
		group.append(p)
		newr = findfromend(places, l, p)
		if newr > rindex: rindex = newr
		j += 1
	i = rindex + 1
	#print group
	groups.append(group)
ans = ''
for g in groups:
	ans +=  str(len(g))+','
print ans[:-1]
