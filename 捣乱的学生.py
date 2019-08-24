import sys
import collections as coll
line = sys.stdin.readline().strip().split()
n = int(line[0])
m = int(line[1])
nums = [int (num) for num in sys.stdin.readline().strip().split()]
counts = coll.Counter(nums)
sb = set()
for num in counts.keys():
    count = counts[num]
    if count > m:
        sb.add(num)

for num in nums:
    if num not in sb:
        print num,
