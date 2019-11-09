import sys
m = input()
n = input()
mat = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    mat[i] = [int(num) for num in sys.stdin.readline().strip().split()]
ret = [float('inf')]*n
ret[0] = 0
for i in range(m):
    for j in range(n):
        if j == 0:
            ret[j] = ret[j] + mat[i][j]
        else:
            ret[j] = min(ret[j], ret[j-1]) + mat[i][j]
print ret[-1]
