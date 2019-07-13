import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())    
    A = []
    B = []
    for i in range(N):
        s = sys.stdin.readline().strip().split(' ')
        A.append(int(s[0]))
        B.append(int(s[1]))
    cur = TreeNode(0)
    global ans
    ans = 'No'
    def InOrder(cur, h, i, added):
	global ans
        if i < N and ans == 'No':            
            a, b = A[i], B[i]
            if h == 2:
                if (a in added) or (b in added):
                    InOrder(cur, h, i+1, added)
            else:
                cur.left = TreeNode(a)
                newadd = list(added)
		newadd.append(a)
		print h, a, b, added, newadd
                InOrder(cur, h + 1, i + 1, newadd)                
                cur.left = None
                
                cur.right = TreeNode(b)
                newadd = list(added)
		newadd.append(b)
		print h, a, b, added, newadd
                InOrder(cur, h + 1, i + 1, newadd)
                cur.right = None
        else:
	    if ans == 'No':
            	ans = added
	   	print added
    InOrder(cur, 0, 0, [])
    if ans != None:
	print ans
    else:
	print 'No'
