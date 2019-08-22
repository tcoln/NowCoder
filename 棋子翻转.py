A = input()
f = input()
for site in f:
        x = site[0]-1
        y = site[1]-1
        if x > 0 and x < 3:
                A[x-1][y] = int(not A[x-1][y])
                A[x+1][y] = int(not A[x+1][y])
        elif x == 0:
                A[x+1][y] = int(not A[x+1][y])
        else:
                A[x-1][y] = int(not A[x-1][y])
        if y > 0 and y < 3:
                A[x][y-1] = int(not A[x][y-1])
                A[x][y+1] = int(not A[x][y+1])
        elif y == 0:
                A[x][y+1] = int(not A[x][y+1])
        else:
                A[x][y-1] = int(not A[x][y-1])
print (A)
