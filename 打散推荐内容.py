import sys
N=input()
M=input()
recs=[]
for i in range(M):
    recs.append(sys.stdin.readline().strip())
ans=[]
tmp = 2
stack = []
for i in range(M):
    if recs[i][0]=='V':
        tmp+=1
        ans.append(recs[i])
    if recs[i][0]=='P':
        stack.append(recs[i])
    if tmp>=N-1 and len(stack)>0:
        tmp=0
        ans.append(stack.pop(0))
print(len(ans))
for i in ans:
    print(i)
