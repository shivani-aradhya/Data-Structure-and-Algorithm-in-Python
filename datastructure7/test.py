class Node:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right= None

def sametree(p,q):
    if p== None and q== None:
        return True
    elif p== None or q==None:
        return False
    elif p.data==q.data:
        return sametree(p.left, q.left) and sametree(p.right,q.right)
    else:
        return False

root1= Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if sametree(root1, root2):
    print("Both trees are identical")
else:
    print("Trees are not identical")
