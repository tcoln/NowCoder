import sys
import numpy as np
line = sys.stdin.readline().strip().split(' ')
N, S = int(line[0]), int(line[1])
MAX = 5000+1
#table = [[-1 for j in range(MAX)] for i in range(MAX)]
table = np.zeros((MAX, MAX)) - 1
print 'init'
def dyamic(n, s, last, table):
    if table[n][s] != -1:
	return table[n][s]
    if n == 1: 
	if s < last:
		#print n, s
        	return 1
	else:
		return 0
    ans = 0
    for i in range(s-n*(n-1)/2, n-1, -1):
        if i < last:
    	    #print n, s, i
            ans += dyamic(n-1, s-i, i, table)
    table[n][s] = ans
    return table[n][s]

ans = dyamic(N, S, S, table)
print ans%1000000007
