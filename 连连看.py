import sys
import copy
from collections import deque
n = 5
mat = [0 for i in range(n)]
mat=[[3, 1, 2, 1, 1],
[1, 1, 1, 1, 3],
[1, 1, 1 ,1 ,1],
[1, 1, 1, 1, 1],
[3, 1, 2, 2, 2]]
#for i in range(n):
	#mat[i] = [int(j) for j in sys.stdin.readline().strip().split()]
global ans
ans = float('inf')

def printm(mat):
	for i in mat:print i

def zhongli_move(mat):
	for i in range(n-2, -1, -1):
		for j in range(n):
			k = i
			while k < n-1 and mat[k][j] != 0 and mat[k+1][j] == 0:
					mat[k+1][j] = mat[k][j]
					mat[k][j] = 0
					k += 1
					
def  backtrack(mat, cand):
	global ans
	if not cand:
		count = 0
		for i in mat: 
			for j in i:
				if j >= 1 and j <= 3: count += 1
		if count < ans: ans = count
		return 
	for can in cand.keys():	
		newmat = copy.deepcopy(mat)
		for pos in cand[can][1:]: newmat[pos[0]][pos[1]] = 0
		zhongli_move(newmat)
		newcand = {}
		visited = [[0 for j in range(n)] for i in range(n)]
		continus(newmat, newcand, visited)
		printm(newmat)
		print newcand
		backtrack(newmat, newcand)
	
def continus(mat, cand, visited):
	for i in range(n):
		for j in range(n):
			if not visited[i][j] and mat[i][j] != 0:
				cand[(i,j)] = [mat[i][j]]
				queue = deque([(i,j)])
				while queue:
					cur = queue.popleft()
					ci, cj = cur[0], cur[1]
					visited[ci][cj] = 1
					cand[(i,j)].append((ci,cj))
					if ci-1>=0 and not visited[ci-1][cj] and cand[(i,j)][0]==mat[ci-1][cj]: queue.append((ci-1,cj))
					if ci+1<n and not visited[ci+1][cj] and cand[(i,j)][0]==mat[ci+1][cj]: queue.append((ci+1,cj))
					if cj-1>=0 and not visited[ci][cj-1] and cand[(i,j)][0]==mat[ci][cj-1]: queue.append((ci,cj-1))
					if cj+1<n and not visited[ci][cj+1] and cand[(i,j)][0]==mat[ci][cj+1]: queue.append((ci,cj+1))
	for can in cand.keys():
		if len(cand[can]) < 1+4: del cand[can]

cands = {}
visited = [[0 for j in range(n)] for i in range(n)]
continus(mat, cands, visited)
printm(mat)
for key in cands.keys():
	print key, cands[key] 	
backtrack(mat, cands)
print ans

