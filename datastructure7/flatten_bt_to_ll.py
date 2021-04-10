class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def flatten(root):
    if root is None:
        return

    flatten((root.left))
    flatten(root.right)

    if root.left is not None:
        current= root.left
        while current.right is not None:
            current= current.right
        current.right= root.right
        root.right= root.left
        root.left= None

    return root

def printpreorder(root):
    if root is None:
        return
    print(root.data)
    printpreorder(root.left)
    printpreorder(root.right)