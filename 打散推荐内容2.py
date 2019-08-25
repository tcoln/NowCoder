import sys
N = input()
M = input()
recs = [0]*M
for i in range(M):
    recs[i] = sys.stdin.readline().strip()
L = 0
for i in range(M-N):
    flag = False
    for j in range(i, i+N):
        if recs[j][0] == 'P':
            if not flag:
                flag = True
            else:
                find = False
                for k in range(j+1, M):
                    if recs[k][0] == 'V':
                        find = True
                        recs.insert(j, recs[k])
                        del recs[k+1]
                        j -= 1
                        break
                if not find:
                    L = j
                    break
print L
for i in recs:
    print i
