class Node:
    def __init__(self, data):
        self.left= None
        self.right= None
        self.data= data

def BST(root , l = None , r = None ):
    if root == None:
        return True
    if (l!= None and l.data >= root.data) or (r!= None and r.data <= root.data):
        return False

    return BST(root.left, l, root) and BST(root.right, root, r)

root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)
if (BST(root, None, None)):
       print("VALID BST")
else:
    print("INVALID BST")



root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
if (BST(root, None, None)):
       print("VALID BST")
else:
    print("INVALID BST")



