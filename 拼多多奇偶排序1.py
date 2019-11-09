import sys
line = sys.stdin.readline().strip().split(';')
nums = [int(i) for i in line[0].split(',')]
N = int(line[1])
evens = []
odds = []
evensNum = 0
for num in nums:
    if num % 2 == 0:
        evens.append(num)
        evensNum += 1
    else:
        odds.append(num)
evens.sort(reverse=True)
odds.sort(reverse=True)
ans = evens[:N]
if evensNum < N:
    ans.extend(odds[:N-evensNum])
ansStr = ''
for i in range(N-1):
    ansStr += str(ans[i]) + ','
print ansStr + str(ans[N-1])
