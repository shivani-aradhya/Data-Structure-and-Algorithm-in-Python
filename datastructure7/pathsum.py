class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def hasPathSum(node, sum):
    if node is None:
        return sum == 0

    else:

        subSum = sum - node.data

        if (subSum == 0 and node.left == None and node.right == None):
            return True


        if node.left is not None:
            return hasPathSum(node.left, subSum)

        if node.right is not None:
            return hasPathSum(node.right, subSum)

    return False

s = 21
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(3)

ans = hasPathSum(root, s)
print(ans)
