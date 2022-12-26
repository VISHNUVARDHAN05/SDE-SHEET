class Stack:
    def __init__(self):
        self.input=[]
        self.output=[]
        self.top1=0
        self.top2=0
    def push(self,x):
        self.input.append(x)
        self.top1=self.top1+1
    def pop(self):
        if self.top1==0 and self.top2==0:
            print("Can not perform POP Operation")
        elif self.top2>0:
            self.output.pop()
            self.top2=self.top2-1
        elif self.top2==0:
            while self.top1!=0:
                self.output.append(self.input.pop())
                self.top1=self.top1-1
                self.top2=self.top2+1
            self.output.pop()
            self.top2=self.top2-1
    def top(self):
        if self.top1==0 and self.top2==0:
            print("Can not perform POP Operation")
        elif self.top2>0:
            self.output.pop()
            self.top2=self.top2-1
        elif self.top2==0:
            while self.top1!=0:
                self.output.append(self.input.pop())
                self.top1=self.top1-1
                self.top2=self.top2+1
            self.output.pop()
            self.top2=self.top2-1