#Using recursion transversal of tree in inorder, preorder and postorder form:
class Node:
    def __init__(self, data):
        self.left= None
        self.right= None
        self.data= data

def Inorder(root):
    if root is not None:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

def Preorder(root):
    if root is not None:
        print(root.data)
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root is not None:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)

root= Node(1)
root.left = Node(2)
root.right= Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)
print("INORDER: ")
Inorder(root)
print("PREORDER: ")
Preorder(root)
print("POSTORDER: ")
Postorder(root)
