import sys
n = int(sys.stdin.readline().strip())
perm = sys.stdin.readline().strip().split(' ')
for i in range(n-1):
    v = int(perm[i])
    print str(n+1-v),
v = int(perm[n-1])
print str(n+1-v)
