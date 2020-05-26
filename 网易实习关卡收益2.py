import sys
def max_profit(profit_list):
   l = len(profit_list)
   if l == 0:
      return 0
   if l <= 2:
      return max(profit_list)
   profits = [profit_list[0]]*l
   profits[1] = max(profit_list[:2])
   for i in range(2, l):
      if profit_list[i] + profits[i-2] < profits[i-1]:
          profits[i] = profits[i-1]
      else:
          profits[i] = profit_list[i] + profits[i-2]
   print(profits) 
   return max(profits)

p = sys.stdin.readline().strip()
p = p[1:len(p)-1]
p = p.split(', ')
l = len(p)
for i in range(l):
   p[i] = int(p[i])
print(max_profit(p))
