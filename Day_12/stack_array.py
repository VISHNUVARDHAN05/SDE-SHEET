class stack:
    def __init__(self):
        self.top=-1
        self.l=[]
        self.size=-1
    def push(self,x):
        self.top=self.top+1
        self.l.append(x)
        self.size=self.size+1
    def pop(self):
        self.l.pop()
        self.size=self.size-1
        self.top=self.top-1

    def size(self):
        return self.size()
    def display(self):
        print(self.l)
s=stack()
s.push(1)
s.display()
s.push(2)
s.display()
s.push(3)
s.display()
s.push(4)
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.pop()
s.display()


