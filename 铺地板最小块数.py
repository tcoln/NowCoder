import sys
T=int(raw_input())
for i in range(T):
	line = raw_input().split(' ')
	N=int(line[0])
	M=int(line[1])
	a=int(line[2])
	print ((N+a-1)/a) * ((M+a-1)/a)
