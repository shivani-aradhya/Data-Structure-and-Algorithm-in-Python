class LNode:
    def __init__(self):
        self.data = None
        self.next = None

class TNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def converttree(head):

    if not head:
        return None

    mid = midfind(head)
    node= TNode(mid.data)

    if mid==head:
        return node
    node.left= converttree(head)
    node.right=converttree(mid.next)
    return node


def midfind(head):
    prev = None
    slow= head
    fast= head

    while fast and fast.next:
        prev= slow
        slow= slow.next
        fast= fast.next.next

    if prev:
        prev.next= None
    return slow