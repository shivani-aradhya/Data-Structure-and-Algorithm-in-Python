from _collections import deque
class Queue:
    def __init__(self):
        self.container= deque()
    def enqueue(self,val):
        self.container.append(val)
        print(self.container)

    def dequeue(self):
        if len(self.container)==0:
            print("Underflow")
        else:
            return self.container.popleft()
    def is_empty(self):
        if len(self.container)==0:
            print("True")
        else:
            print("False")
q = Queue()
print("Is queue empty:")
q.is_empty()
q.enqueue(10)
q.enqueue(20)
q.enqueue(70)
q.dequeue()
q.dequeue()
print("After Dequeue:")
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()

