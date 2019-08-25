import sys
s = sys.stdin.readline().strip()
s1 = s.replace('=', '-(') + ')'
var = 'X'
c = eval(s1, {var:1j})
print (int(-c.real/c.imag))
