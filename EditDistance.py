import sys
try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        A = s.split(' ')[0]
        B = s.split(' ')[1]
        m = len(A)
        n = len(B)
        edit = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            edit[i][0] = i
        for j in range(n+1):
            edit[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                flag = 0 if A[i-1] == B[j-1] else 1
                edit[i][j] = min(edit[i-1][j]+1, edit[i][j-1]+1, edit[i-1][j-1]+flag)
        print edit[m][n]
except:
    pass
