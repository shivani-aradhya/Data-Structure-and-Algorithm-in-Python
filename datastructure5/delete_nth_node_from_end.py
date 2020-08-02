#Remove Nth Node From End of List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def countlist(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def removenode(self, n):
        fast = self.head
        slow = self.head
        for i in range(n):
            if fast.next is None:
                self.head = self.head.next
                return self.head
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next


l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
print("Linked list: ")
l.printlist()
a = int(input("Node you wanna remove? "))
if a > l.countlist():
    print("What node should I delete if it doesn't exist so deleting last node from end")

l.removenode(a)

print("Linked List after Removal ")
l.printlist()







