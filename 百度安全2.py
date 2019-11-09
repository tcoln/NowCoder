def  maxProfit(prices):
	maxp = 0
	if not prices or len(prices) == 1:return maxp
	l = len(prices)
	stack = [prices[0]]
	i = 1
	while stack and i < l:
		print stack
		top = stack[-1]
		if prices[i] >= top:
			stack.append(prices[i])
		else:
			if top - stack[0] > maxp:
				maxp = top - stack[0]
			while stack and prices[i] < stack[-1]:
				stack.pop()
			stack.append(prices[i])
		i += 1
	if stack and stack[-1] - stack[0] > maxp:
		maxp = stack[-1] - stack[0]
	return maxp

ps = [[11,22,2,4,56,3,1], [56,3,1],[1,3,5,2,4,6]]
for p in ps:
	print p
	print maxProfit(p)
