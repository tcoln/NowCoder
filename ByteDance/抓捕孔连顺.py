'''
https://www.nowcoder.com/question/next?pid=16516564&qid=362294&tid=24748889
抓捕孔连顺
双指针遍历，查找到i前面D范围内的j,然后计算i为第一个点，j-i个位置抽两个点的组合数
注意下一次的j可以利用上一次的j的位置继续查找，不用从i+1开始
'''
s = raw_input()
N = int(s.split(' ')[0])
D = int(s.split(' ')[1])
s = raw_input()
fs = s.split(' ')
nums = []
for f in fs:
    nums.append(int(f))
ans = 0L
j = 1
for i in range(N-2):
    while j < N and nums[j] - nums[i] <= D:
        j += 1
    j -= 1
    if j-i>=2:
        ans +=  (j-i-1)*(j-i)/(2*1)
    #print ans
if ans > 99997867:
    ans = ans % 99997867
print ans
