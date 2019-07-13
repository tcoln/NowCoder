#评测题目: 
#输入一组数字，实现一个算法，可以找出这组数中的“异数”，“异数”是指与左右相邻的数都不相同，输入的数字中最多只有一个“异数”。
#如输入的 {1，1，3，3，-4，-4，6，9，9，0，0}，6为其中的“异数”，
#{1，1，1，2，2，2，3，4，4，5，5}，3为其中的”异数”，{2，2，3，3，4，4，5，5}无“异数”，存在两个异数作报错处理。

def diffNum(nums):
  l = len(nums)
  if nums == None or l <= 2:
    return 'error'
  diff = None
  for i in range(1, l-1):
    if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
      if diff == None:
      	diff = nums[i]
      else:
        return 'error'
  return diff

if __name__ == '__main__':
  a = [1,1,3,3,-4,-4,6,9,9,0,0]
  print diffNum(a)
  a = [1,1,3,3,-4,-4,6,6,9,9,0,0]
  print diffNum(a)
  a = [1,1,3,3,-4,-4,6,9,9,7,0]
  print diffNum(a)
