class MaxStack:
    def __init__(self):
        self.stack= []
        self.tempstack=[]

    def push(self, data):
        self.stack.append(data)

        if len(self.stack)==1:
            self.tempstack.append(data)
            return
        if data> self.tempstack[-1]:
            self.tempstack.append(data)
        else:
            self.tempstack.append(self.tempstack[-1])

    def getmax(self):
        return self.tempstack[-1]

    def pop(self):
        self.stack.pop()
        self.tempstack.pop()

s= MaxStack()
s.push(10)
s.push(20)
print(s.getmax())
s.push(30)
print(s.getmax())
s.push(40)
print(s.getmax())
s.pop()
print("After popping max element:" , s.getmax())
