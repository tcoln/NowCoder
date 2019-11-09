import sys

def isLegel(nums):
    legel = False
    l = len(nums)
    firstL = len(nums[0])
    rule11 = True
    rule12 = True
    for i in range(l):
        if not (len(nums[i]) - (i%2) == 1):
            rule11 = False
        if not (len(nums[i]) + (i%2) == 2):
            rule12 = False
    rule2 = len(nums[0]) == 2 and len(nums[-1]) == 2
    for i in range(1,l-1):
        if not len(nums[i]) == 1:
            rule2 = False
    rule3 = len(nums[0]) == 1 and len(nums[-1]) == 1
    for i in range(1,l-1):
        if not len(nums[i]) == 2:
            rule3 = False
    print rule11, rule12, rule2, rule3
    legel = rule11 or rule12 or rule2 or rule3
    return 'true' if legel else 'false'
    
while True:
    line = sys.stdin.readline()
    if not line: break
    nums = line.strip().split()
    print isLegel(nums),
