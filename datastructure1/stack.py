#Testcases used
class Stack:
    def __init__(self):
        self.container= []
    def push(self,val):
        self.container.append(val)
        print(self.container)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]


    def is_empty(self):
        if len(self.container)==0:
            print("True")
        else:
            print("False")


s= Stack()
print("Is stack empty?")
s.is_empty()
s.push(5)
s.push(10)
s.pop()
s.pop()
s.push(15)
s.push(20)
print("Is stack empty?")
s.is_empty()






