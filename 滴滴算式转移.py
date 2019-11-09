import sys
words = "3 + 2 + 1 + -4 * -5 + 3 / 1 + 3 + 9 + 1".split()  #sys.stdin.readline().strip().split()
N = len(words) / 2 + 1
operas = []
nums = []
ans = []
preo = ''
print words
for word in words:
	if word in '+-*/':
		operas.append(word)
		if preo != '' and word != preo:
			if preo in '*+':
				tmp = nums.pop()
				nums.sort()
				ans.extend(nums)
				nums = [tmp]
			else:
				#nums.sort()
                        	ans.extend(nums)
                        	nums = []
		preo = word
	else:
		nums.append(int(word))
	print word, nums, operas, ans
print ans, operas
if operas[-1] in '*+':
	nums.sort()
ans.extend(nums)
for i in range(N-1):
	print str(ans[i]) + ' ' + operas[i] + ' ',
print ans[N-1]
