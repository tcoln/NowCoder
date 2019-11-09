def maxbst(root):
    if not root:
        return 0
    num = ln = rn = 0
    bst, num = isbst(root)
    if not bst:
        lbst, ln = maxbst(root.left)
        rbst, rn = maxbst(root.right)
    return max([num, ln, rn])

# 要后续遍历节省重复计算
def isbst(root):
    if not root:
        return (True, 0)
    flagl, ln = isbst(root.left)
    flagr, rn = isbst(root.right)
    l = if root.left: root.left.val else float('-inf')
    r = if root.right: root.right.val else float('inf')
    flag = l <= root.val and root.val <= r
    return (flag and flagl and flagr, ln+rn+1) 
