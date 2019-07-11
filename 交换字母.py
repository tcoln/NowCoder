import sys
line = sys.stdin.readline().strip().split(' ')
s = line[0]
m = int(line[1])
N = len(s)
maxL = 0
charPos = {} 
for i in range(N):
    if charPos.has_key(s[i]):
        charPos[s[i]].append(i)
    else:
        charPos[s[i]] = [i]
for key in charPos.keys():
    pos = charPos[key]
    posN = len(pos)
    for c in range(posN):
        moves = []
        for j in range(posN):
            moves.append(max(abs(pos[j]-pos[c]) - 1 - (abs(j-c)-1), 0))
        moves.sort()
        totalM = 0
        contiL = 0
        for j in moves:
            totalM += j
            if totalM > m:
                break
            else:
                contiL += 1
                if contiL > maxL:
                    maxL = contiL
print maxL
