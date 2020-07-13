class Queue:
    def __init__(self):
        self.s= []

    def enqueue(self, data):
        self.s.append(data)

    def dequeue(self):
        if len(self.s)<=0:
            print("QUEUE IS EMPTY")

        current_data = self.s[len(self.s)-1]
        self.s.pop()

        if len(self.s)<=0:
            return current_data
        item= self.dequeue()

        self.s.append(current_data)
        return item

q= Queue()
q.enqueue(9)
q.enqueue(8)
q.enqueue(7)
print("QUEUE: ")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

