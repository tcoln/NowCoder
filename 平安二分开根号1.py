import sys
line = sys.stdin.readline().strip().split()
a = float(line[0])
b = int(line[1])
l = 0
r = a
ans = (l+r) / 2
while ans**b != a:
    if ans**b < a:
        l = ans
    else:
        r = ans
    if abs(ans-(l+r)/2) < 0.0000001:
        break
    ans = (l+r)/2 
print ('%.6f'%ans)
