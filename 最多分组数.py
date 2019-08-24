import sys
import bisect as bi
C = input()
for i in range(C):
    roles = [int (num) for num in sys.stdin.readline().strip().split()]
    T = roles[0]
    del roles[0]
    ans = 0
    roles.sort()
    while T > 2 and roles[0] == 0:
	del roles[0]
	T -= 1
    while T > 2:
        ans += 1
        roles[0] -= 1
        roles[-1] -= 1
        roles[-2] -= 1
        tmp = roles[-2:]
        del roles[-2]
        del roles[-1]
        index = bi.bisect(roles, tmp[0])
        roles.insert(index, tmp[0])
        index = bi.bisect(roles, tmp[1])
        roles.insert(index, tmp[1])
        while T > 2 and roles[0] < 1:
            del roles[0]
            T -= 1
	print ans, roles, T
    print ans
