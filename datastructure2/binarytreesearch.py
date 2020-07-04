class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right = None

    def insert(self, data):
        if self.data:
            if data< self.data:
                if self.left is None:
                    self.left= Node(data)
                else:
                    self.left.insert(data)
            elif data> self.data:
                if self.right is None:
                    self.right= Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data= data

    def find(self, val):
        if val<self.data:
            if self.left is None:
                return str(val) + " Not In Tree"
            return self.left.find(val)
        elif val> self.data:
            if self.right is None:
                return str(val) + " Not in Tree"
            return self.right.find(val)
        else:
            return str(val) + " Present in Tree"
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()


root= Node(25)
root.insert(7)
root.insert(30)
root.insert(40)
root.insert(20)

root.printtree()

print(root.find(5))
print(root.find(30))
print(root.find(20))