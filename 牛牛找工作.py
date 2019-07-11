import sys
import bisect
line = sys.stdin.readline().strip().split(' ')
N = int(line[0])
M = int(line[1])
jobs = []
for i in range(N):
    line = sys.stdin.readline().strip().split(' ')
    jobs.append([int(line[0]), int(line[1])])
jobs.sort(key=lambda item:item[0])
onlyjobs = []
for i in jobs:
    onlyjobs.append(i[0])
for i in range(1, N):
    if jobs[i-1][1] > jobs[i][1]:
        jobs[i][1] = jobs[i-1][1]
A = sys.stdin.readline().strip().split(' ')
for a in A:
    a = int(a)
    pos = bisect.bisect_right(onlyjobs, a)
    pos -= 1
    if pos < 0:
        print 0
    else:
        print jobs[pos][1]
