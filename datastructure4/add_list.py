class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add2list(self, first , second):
        prev = None
        temp = None
        carry = 0

        while (first is not None or second is not None):
            if first is None:
                fdata =0
            else:
                fdata = first.data
            if second is None:
                sdata =0
            else:
                sdata = second.data

            sum = carry + fdata + sdata
            if sum >=10:
              carry =1
            else:
              carry =0

            if sum <10:
                sum= sum
            else:
                sum= sum % 10

            temp = Node(sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

first = LinkedList()
first.push(4)
first.push(1)
first.push(3)
first.push(7)
print("FIRST LIST: ")
first.printlist()
second = LinkedList()
second.push(4)
second.push(3)
second.push(9)
second.push(1)
print("SECOND LIST: ")
second.printlist()

res= LinkedList()
res.add2list(first.head,second.head)
print("ADDITION OF TWO LISTS: ")
res.printlist()















