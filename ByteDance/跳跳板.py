#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
        
def InOrder(tour, N, depth):
    pos = tour[-1]
    if pos == N-1:
        global ans
        ans = depth
        return 1
    step = steps[pos]
    for s in range(-step, step+1):
        nextpos = pos + s
        if s != 0 and nextpos >= 0  and nextpos < N and nextpos not in tour and steps[nextpos] != 0:
            newtour = list(tour)
            newtour.append(nextpos)
            InOrder(newtour, N, depth+1)
            
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N, P = int(line.split(' ')[0]), int(line.split(' ')[1])
    line = sys.stdin.readline().strip()
    steps = [int(s) for s in line.split(' ')]
    global ans
    ans = -1
    InOrder([P-1], N, 0)
    print ans
