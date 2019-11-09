import sys
def EditDistance(A, B):
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
    return edit[m][n]

def getSub(A, sub, preI, lens, allsub):
    if len(sub) == lens and sub not in allsub:
        allsub.append(sub)
    l = len(A)
    for i in range(l):
        if i > preI:
            newsub = sub+A[i]
            getSub(A, newsub , i, lens, allsub)

def SplitSub(minl, maxl, distance, A, B):
    m = len(A)
    n = len(B)
    ans = 0
    for i in range(minl, maxl+1):
        subAs = []
        subBs = []
        getSub(A, '', -1, i, subAs)
        getSub(B, '', -1, i, subBs)
	print i, subAs, subBs
        for subA in subAs:
            for subB in subBs:
                if EditDistance(subA, subB) <= distance:
                    print subA, subB, EditDistance(subA, subB), distance
                    ans += 1
    return ans

distance = input()
minl= input()
maxl = input()
A = sys.stdin.readline().strip().split(',')
B = sys.stdin.readline().strip().split(',')
dA = {}
dB = {}
na = nb = 0
for i in A:
    if i not in dA:
        dA[i] = str(na)
        na += 1
for i in B:
    if i not in dB:
        dB[i] = str(nb)
        nb += 1
newA = [dA[i] for i in A]
newB = [dB[i] for i in B]
print newA, newB
print SplitSub(minl, maxl, distance, newA, newB)

