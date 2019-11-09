import sys
line = sys.stdin.readline().strip().split()
n, m = int(line[0]), int(line[1])
global ans
ans = 0
def backt(path, n, m, k):
    global ans
    print path, n, m
    if n == 0:
        ans += 1 if m == 0 else 0
	return 
    for i in range(k):
        if i in path:
            path.append(i)
            backt(path, n-1, m, k)
        else:
            path.append(i)
            backt(path, n-1, m-1, k)
        path.remove(i)
backt([], n, m, m)
print ans
