import sys
n = 3 #int(sys.stdin.readline().strip())
m = 3 #int(sys.stdin.readline().strip())
mat = [[-2, -3, 3], [-5, -10, 1], [0, 30, -5]] #[[0 for j in range(m)] for i in range(n)]
#nums = sys.stdin.readline().strip().split()
#for i in range(n*m): mat[i/m][i%m] = int(nums[i])
needs = [[0 for j in range(m)] for i in range(n)]
remains = [[0 for j in range(m)] for i in range(n)]
needs[0][0] = 0 if mat[0][0] > 0 else 1-mat[0][0]
remains[0][0] = mat[0][0] if mat[0][0] > 0 else 1
for j in range(1, m):
    i = 0
    needs[i][j] = needs[i][j-1] + (1-(remains[i][j-1] + mat[i][j]) if remains[i][j-1] + mat[i][j] <= 0 else 0)
    remains[i][j] = 1 if remains[i][j-1] + mat[i][j] <= 0 else remains[i][j-1] + mat[i][j]
for i in range(1, n):
    j = 0
    needs[i][j] = needs[i-1][j] + (1-(remains[i-1][j] + mat[i][j]) if remains[i-1][j] + mat[i][j] <= 0 else 0)
    remains[i][j] = 1 if remains[i-1][j] + mat[i][j] <= 0 else remains[i-1][j] + mat[i][j]
for i in range(1,n):
    for j in range(1,m):
        needup = needs[i-1][j] + (1-(remains[i-1][j] + mat[i][j]) if remains[i-1][j] + mat[i][j] <= 0 else 0)
        needleft = needs[i][j-1] + (1-(remains[i][j-1] + mat[i][j]) if remains[i][j-1] + mat[i][j] <= 0 else 0)
        needs[i][j] = min(needup, needleft)
        if needup > needleft:
            leftremain = 1 if remains[i][j-1] + mat[i][j] <= 0 else remains[i][j-1] + mat[i][j]
	    remains[i][j] = leftremain
        elif needup < needleft:
            upremain = 1 if remains[i-1][j] + mat[i][j] <= 0 else remains[i-1][j] + mat[i][j]
	    remains[i][j] = upremain
        else:
            remains[i][j] = max(upremain, leftremain)
for i in range(n):
	print mat[i]
print ''
for i in range(n):
	print remains[i]
print ''
for i in range(n):
	print needs[i]
print ''
print needs[n-1][m-1]
