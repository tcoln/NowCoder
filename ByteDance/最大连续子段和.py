s=[7,-8,4]
l = len(s)
indexs = [0 for i in range(l)]
sums = [0 for i in range(l)]
sums[0] = s[0]
for i in range(1, l):
    if sums[i-1] > 0:
        sums[i] = sums[i-1] + s[i]
        indexs[i] = indexs[i-1]
    else :
        sums[i] = s[i]
        indexs[i] = i
m = max(sums)
i = sums.index(m)
print m
print indexs[i], i
