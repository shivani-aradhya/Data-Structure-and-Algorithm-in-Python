# Python code to convert a sorted array
# to a balanced Binary Search Tree

# binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if arr is None:
        return None


    mid = (len(arr)) // 2


    root = Node(arr[mid])


    root.left = sortedArrayToBST(arr[:mid])


    root.right = sortedArrayToBST(arr[mid + 1:])
    return root







