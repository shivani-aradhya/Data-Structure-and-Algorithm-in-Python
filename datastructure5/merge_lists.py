# Definition for singly-linked list.
#Recursive Approach
class ListNode:
     def __init__(self, data=0, next=None):
         self.data = data
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newdata):
        newnode= ListNode(newdata)

        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode

    def printList(self):
            temp = self.head

            while temp:
                print(temp.data)
                temp = temp.next


def mergeTwoLists(head1, head2):
    temp = None
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeTwoLists(head1.next, head2)

    else:
        temp = head2
        temp.next = mergeTwoLists(head1, head2.next)

    return temp

l1 = LinkedList()
l1.append(1)
l1.append(3)
l1.append(5)
l1.append(7)
l1.append(9)

l2 = LinkedList()
l2.append(2)
l2.append(4)
l2.append(6)
l2.append(8)
l2.append(10)


l3 = LinkedList()
l3.head = mergeTwoLists(l1.head,l2.head)

print(" Two Merged Linked List is : ")
l3.printList()





