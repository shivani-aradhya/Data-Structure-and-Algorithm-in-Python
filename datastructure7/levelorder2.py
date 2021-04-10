class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right = None


def levelorder(root):
    if root is None:
        return []

    queue= [root]
    result=[]

    while(len(queue)!= 0):
        l=[]
        for i in range(len(queue)):
            temp= queue.pop(0)
            l.append(temp.data)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

            result.insert(0,l)
    return result

