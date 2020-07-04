#Test case used where a b c d are inserted in linked list.
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def add(self, data):

        new_node = Node(data)
        if (self.head):
            current=self.head
            while current.next:
                current=current.next
            current.next= new_node
        else:
            self.head=new_node


    def printlist(self):
        val= self.head
        while (val):
            print(val.data)
            val=val.next

ll= LinkedList()
ll.add("a")
ll.add("b")
ll.add("c")
ll.add("d")
print("Our list:")
ll.printlist()
