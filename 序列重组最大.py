import sys
import collections as coll
line = sys.stdin.readline().strip().split(' ')
N, M = int(line[0]), int(line[1])
nums1 = [int(num) for num in sys.stdin.readline().strip().split(' ')]
nums2 = [int(num) for num in sys.stdin.readline().strip().split(' ')]
nums2 = set(nums2)
nums2 = coll.Counter(nums2)
print nums1, nums2
ans = []
for m in range(M-1, -1, -1):
	for num in nums1:
		if not nums1:
			break
		bushu = m - num if m - num >= 0 else m - num + M
		if bushu in nums2:
			print m, bushu
			ans.append(m)
			nums1.remove(num)
			#nums2.discard(bushu)
			nums2.remove(bushu)
		print nums1, nums2
for num in ans:
	print str(num) + ' ',
