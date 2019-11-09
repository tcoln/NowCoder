import sys
line = sys.stdin.readline()
#line = sys.stdin.readline().strip()
low = line.lower()
rev = low.replace(' ', '0')
print rev[::-1]
