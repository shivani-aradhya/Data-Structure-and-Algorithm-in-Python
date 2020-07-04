class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.item)
        if self.right:
            self.right.printtree()

def countnodes(root):
        if root is None:
           return 0
        else:
            return (1 + countnodes(root.left) + countnodes(root.right))

def complete_tree( root, index, numbernodes):
     if root is None:
         return True
     if index>= numbernodes:
         return False
     return (complete_tree(root.left, 2 * index + 1, numbernodes) and complete_tree(root.right, 2 * index + 2, numbernodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.printtree()

node_count = countnodes(root)
index = 0

if complete_tree(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")


