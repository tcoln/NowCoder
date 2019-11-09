class Node(object): 
    def __init__(self, val):
      self.data = val
      self.next = None

def print_middle_element(head):  
    if not head:
      return None
    p1 = None
    p2 = head
    while p2 and p2.next:
      if not p1:
        p1 = head
      else:
        p1 = p1.next
      p2 = p2.next.next
    if p2:
	if not p1:
          return p2.data 
        else:	
          return p1.next.data
    else:
      	return (p1.data, p1.next.data)

l = [1,2,3,4,5,6]
l = [1]
head = None
pre = None
for i in l:
	cur = Node(i)
	if not head:
		head = cur
		pre = cur
	else:
		pre.next = cur
		pre = cur
cur = head
print 'LinkList:',
while cur:
	print cur.data,
	cur = cur.next
print ' meddle element:' , print_middle_element(head)
