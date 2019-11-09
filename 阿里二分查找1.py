def binarySearch(A, target, n):
  left = 0
  right = n-1
  index = -1
  while left <= right:
  	m = (left+right)/2
  	if A[m] < target:
  		left = m + 1
  	elif A[m] > target:
  		right = m - 1
  	else:
  		index = m
  		break
  return index

A = [1,2,3,4,5]
print A
print 'input find target:'
target = input()
n = len(A)
print binarySearch(A, target, n)
