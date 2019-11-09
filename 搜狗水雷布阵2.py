import sys
def dfs(x, y, up_down, visited, isPass, R):
    if (up_down == 1 and abs(y-0) <= R) or (up_down == 0 and abs(y-100) <= R):
        isPass[0] = False
        return
    for i in range(N):
        if not visited[i] and ((dotxs[i]-x)**2 + (dotys-y)**2)**0.5 <= 2*R:
            visited[i] = 1
            dfs(dotxs[i], dotys[i], up_down, visited, isPass, R)
def solve(N,R,D,dotxs,dotys):
    isPass = [True]
    visited = [0]*N
    for i in range(N):
        if not visited[i] and abs(dotys[i]-100) <= R:
            visited[i] = 1
            dfs(dotxs[i], dotys[i], 1, visited, isPass, R)
        if not visited[i] and abs(dotys[i]-0) <= R:
            visited[i] = 1
            dfs(dotxs[i], dotys[i], 0, visited, isPass, R)
    if D == 0:
        return 'Y' if isPass[0] else 'N'
    else:
        return 2
for f in range(1):
    for line in sys.stdin:
        print line,
        #a = line.split()
        #line = sys.stdin.readline()
        if not line or line == '' or line=='EOF': break
        line = line.strip().split()
        N = int(line[0])
        R = float(line[1])
        D = float(line[2])
        dotxs = []
        dotys = []
        for i in range(3, 2*N+3, 2):
            dotxs.append(float(line[i]))
            dotys.append(float(line[i+1]))
        print (solve(N,R,D,dotxs,dotys))
