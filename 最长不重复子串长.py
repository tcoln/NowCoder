import sys
def MaxLen(s):
    ans = 0
    if not s or len(s) == 0:
        return ans
    strD = {}
    tmp = 0
    start = 0
    for i in range(len(s)):
        if s[i] in strD:
		if strD[s[i]] >= start:
            		start = strD[s[i]] + 1
        tmp = i - start + 1
        strD[s[i]] = i
        ans = max(ans, tmp)
    return ans
print MaxLen(sys.stdin.readline().strip())
