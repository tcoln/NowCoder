# https://www.nowcoder.com/question/next?pid=16516564&qid=362292&tid=24748889
'''
https://www.nowcoder.com/question/next?pid=16516564&qid=362292&tid=24748889
特征提取
维护一个最新的字典，该字典只存储当前特征，并更新最长长度
'''
from copy import deepcopy
N=int(raw_input())
M=int(raw_input())
maxL = 0
fd = {}
for i in range(M):
    newfd = {}
    line=raw_input().split(' ')
    for j in range(int(line[0])):
        f = (int(line[2*j+1]), int(line[2*j+2]))
        fd[f] = fd.get(f, 0) + 1
        newfd[f] =  fd.get(f, 0)
        if fd[f] > maxL:
            maxL = fd[f]
    #print fd, newfd
    fd = newfd
print maxL

