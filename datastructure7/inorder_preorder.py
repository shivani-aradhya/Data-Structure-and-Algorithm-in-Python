class Node:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right= None


def buildtree(inorder, preorder):
    if len(inorder)==0:
        return
    if len(preorder)==1:
        return Node(preorder[0])

    root_val= preorder.pop(0)
    root= Node(inorder[root_val])
    index_root= inorder.index(root_val)

    root.left = buildtree(preorder, inorder[:index_root])  # 4
    root.right = buildtree(preorder, inorder[index_root + 1:])
    return root


inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildtree.preIndex = 0
root = buildtree(inOrder, preOrder)

# Let us test the build tree by priting Inorder traversal
print("Inorder traversal of the constructed tree is")
print(root)