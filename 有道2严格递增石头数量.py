import sys
T = input()
for t in range(T):
    line = sys.stdin.readline().strip().split()
    n, m = int(line[0]), int(line[1])
    nums = [int(num) for num in sys.stdin.readline().strip().split()]
    ret = 'YES'
    for i in range(n):
        m += nums[i] - i
        if m < 0:
            ret = 'NO'
            break
    print ret
