#Perfect Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next= None

def connect(root):
    if not root:
        return None

    q= [root]

    while q:
        curr = q.pop(0)
        if curr.left and curr.right:  #if curr.left
            curr.left.next= curr.right
            if curr.next:
                curr.right.next= curr.next.left

            q.append(curr.left)
            q.append(curr.right)

    return root


