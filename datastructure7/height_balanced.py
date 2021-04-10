class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None

def heightbalance(root):

    if root is None:
        return 0,True

    l_height, l_balance= heightbalance(root.left)
    r_height, r_balance = heightbalance(root.right)

    return (max(l_height,r_height)+1), l_balance and r_balance and abs(l_height-r_height<=1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if heightbalance(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")



