class Node:
    def __init__(self, data):
        self.left= None
        self.right= None
        self.data= data

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def height_balanced(root):
    if root is None:
        return True

    left = height(root.left)
    right = height(root.right)
    if (left - right == 0) or (left - right == 1) or (left - right == -1):
        if height_balanced(root.left) is True and height_balanced(root.right) is True:
            return True
        else:
            return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.left = Node(7)
if height_balanced(root):
    print("BALANCED TREE ")
else:
    print("NOT BALANCED TREE ")
