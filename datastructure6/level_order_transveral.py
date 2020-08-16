class Node:
    def __init__(self, data):
        self.left= None
        self.right= None
        self.data= data

class Solution:
    def levelorder(self, root):
        if root is None:
          return []
        current = [root]
        output = []
        while current:
            value =[]
            level = []
            for node in current:
                value.append(node.data)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                current = level
            output.append(value)
        return output

root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)
result = Solution().levelorder(root)
print(result)



