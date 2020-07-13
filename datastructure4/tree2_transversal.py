#Inorder, preorder and postorder transversal in iterative form.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def Inorder(root):
    current = root
    stack =[]
    while True:
        if current is not None:
            stack.append(current)
            current= current.left
        elif(stack):
            current= stack.pop()
            print(current.data)
            current= current.right
        else:
            break

def Preorder(root):
    if root is None:
        return
    stack = []
    stack.append(root)

    while stack:
        current = stack.pop()
        print(current.data)
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)

def Postorder(root):
    if root is None:
        return
    stack1= []
    stack2= []

    stack1.append(root)
    while stack1:
        temp= stack1.pop()
        stack2.append(temp)

        if temp.left:
            stack1.append(temp.left)
        if temp.right:
            stack1.append(temp.right)

    while stack2:
        temp = stack2.pop()
        print(temp.data)





root= Node(1)
root.left = Node(2)
root.right = Node(3)
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
