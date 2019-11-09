import sys
import collections as coll
import heapq
T = input()
for t in range(T):
    n = input()
    nums = [int(num) for num in sys.stdin.readline().strip().split()]
    d = coll.Counter(nums)
    keys = [-v for v in d.values()]
    heapq.heapify(keys)
    l = len(keys)
    while l >= 2:
        key1 = heapq.heappop(keys)
        key2 = heapq.heappop(keys)
        key1 += 1
        key2 += 1
        if key1 == 0:
            l -= 1
        else:
            heapq.heappush(keys, key1)
        if key2 == 0:
            l -= 1
        else:
            heapq.heappush(keys, key2)
	print keys
    print 'NO' if keys else 'YES'
    # 1 1 1 2 2 2 2 5
