import sys
T = input()
for t in range(T):
    line = sys.stdin.readline().strip().split()
    n, k = int(line[0]), int(line[1])
    nums = [int(num) for num in sys.stdin.readline().strip().split()]
    ret = 'YES'
    base = 0
    hasSuper = True
    useSuper = False
    while True:
        nexth = -1
        baseh = float('inf') if useSuper else nums[base]
        if useSuper:
            useSuper = False
        for i in range(1,k+1):
            if base+i < n and nums[base+i] <= baseh:
                if nums[base+i] > nexth:
                    nextb = base + i
                    nexth = nums[nextb]
        if nexth != -1:
            base = nextb
            if base >= n-1:
                break
        elif hasSuper:
            hasSuper = False
            useSuper = True
        else:
            break
    if base < n-1:
        ret = 'NO'
    print ret
