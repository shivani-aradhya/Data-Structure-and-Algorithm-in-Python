class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def helper(root,sum_total,lst,result):
    if root.left is None and root.right is None:
        if sum_total==root.data:
            result+= [lst + [root.data]]

    if root.left:
        helper(root.left, sum_total - root.val, lst + [root.data], result)
    if root.right:
        helper(root.right, sum_total - root.val, lst + [root.data], result)
    return result


def PathSum(node, sum):
    if node is None:
        return []
    return helper(node,sum,[],[])




