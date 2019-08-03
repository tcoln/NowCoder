import sys
T = int(sys.stdin.readline().strip())

def backtrack(perm, depth, candi):
    find = False
    if depth >= n:
        find = True
        return find
    l = len(candi)
    for i in range(l):
        num = nums[i]
        if depth >= 2:
            if perm[-1] < perm[-2] + num and num < perm[0] + perm[-1] and perm[0] < perm[1] + num:
                perm.append(num)
                del candi[i]
                find  = find or backtrack(perm, depth+1, candi)
                del perm[-1]
                candi.insert(i, num)
        else:
            perm.append(num)
            del candi[i]
            find  = find or backtrack(perm, depth+1, candi)
            del perm[-1]
            candi.insert(i, num)
    return find

for t in range(T):
    n = int(sys.stdin.readline().strip())
    nums = [int(num) for num in sys.stdin.readline().strip().split(' ')]
    d = {}
    for num in nums:
        if d.has_key(num):
            d[num] += 1
        else:
            d[num] = 1
    ans = backtrack([], 0, nums)
    if ans:
        print 'YES'
    else:
        print 'NO'
