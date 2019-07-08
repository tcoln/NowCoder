n = raw_input()
N = int(n)
for i in range(N):
    s = raw_input()
    L = list(s)
    l = len(s)
    if l >= 3:
        j = 0
        while j < l-2:
            if L[j] == L[j+1] and L[j] == L[j+2]:
                del L[j]
                l -= 1
                continue
            if L[j] == L[j+1] and j+3 < l and L[j+2] == L[j+3] and L[j+1] != L[j+2] :
                del L[j+2]
                l -= 1
                continue
            #print L, j
            j += 1
    ans = ''
    for j in L:
        ans += str(j)
    print ans
