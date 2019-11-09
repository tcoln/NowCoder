import sys
N = input()
posN = 0
fenzi = 0
label_scores = []
for i in range(N):
	line = sys.stdin.readline().strip().split()
	label_scores.append((int(line[0]), float(line[1])))
label_scores.sort(key=lambda item:item[1], reverse=True)
for i in range(N):
	if label_scores[i][0] == 1:
		posN += 1
	else:
		fenzi += posN
fenmu = (N-posN)*posN
if posN == 0:
	ans = 0
elif posN == N:
	ans = 1
else:
	ans = fenzi*1.0/fenmu
print ('%.2f'%ans)
