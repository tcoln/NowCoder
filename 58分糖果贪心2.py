N = input()
scores = []
for i in range(N):
    scores.append(input())
ret = [1]*N
for i in range(1, N):
    if scores[i] > scores[i-1]:
        ret[i] = ret[i-1] + 1
    else:
        ret[i] = 1
for i in range(N-2, -1, -1):
    if scores[i] > scores[i+1] and ret[i] <= ret[i+1]:
        ret[i] = ret[i+1] + 1
print sum(ret)
