#Reversing Linked list
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def push(self, newdata):
        newnode= Node(newdata)
        newnode.next= self.head
        self.head= newnode

    def print(self):
        value= self.head
        while(value):
            print(value.data)
            value = value.next

    def reverse(self):
        previous= None
        current = self.head
        while(current):
            next= current.next
            current.next= previous
            previous= current
            current = next
        self.head = previous

ll= LinkedList()
ll.push(20)
ll.push(10)
ll.push(15)
ll.push(20)
ll.push(5)
ll.push(25)
print("LINKED LIST: ")
ll.print()
ll.reverse()
print("REVERSE LINKED LIST: ")
ll.print()



