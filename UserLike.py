import sys
import bisect
n = int(raw_input())
likes = {}
s = raw_input().strip().split(' ')
for i in range(n):
    like = int(s[i])
    if likes.has_key(like):
        likes[like].append(i)
    else:
        likes[like] = [i]
#print likes
q = int(raw_input())
for line in range(q):
    s = raw_input().strip().split(' ')
    l = int(s[0])-1
    r = int(s[1])-1
    k = int(s[2])
    count = 0
    if likes.has_key(k):
        indexs = likes[k]
        #for i in indexs:
        #    if i >= l and i <= r: 
        #        count += 1
	l = bisect.bisect_left(indexs, l)
	r = bisect.bisect_right(indexs, r)
	print indexs, l, r	
	count = r-l
    	print count
    else:
	print 0
