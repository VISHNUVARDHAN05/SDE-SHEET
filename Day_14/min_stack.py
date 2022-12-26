class Stack:
    def __init__(self):
        self.s=[]
        self.mini=99999999
    def push(self,ele):
        if len(self.s)==0:
            self.s.append(ele)
            self.mini=ele
        else:

            if ele<self.mini:
                val=2*ele-self.mini
                self.s.append(val)
                self.mini=ele
            else:
                self.s.append(ele)


    def pop(self):
        if len(self.s)==0:
            return -1
        ele=self.s.pop()
        if ele<self.mini:
            self.mini=2*(self.mini)-ele

    def top(self):
        if len(self.s)==0:
            return -1
        val=self.s[-1]
        if val<self.mini:
            return self.mini
        return val
    def getmini(self):
        print(self.mini)
        return self.mini
    def display(self):
        print(self.s)

s1=Stack()
s1.push(-2)
s1.display()
s1.push(0)
s1.display()
s1.push(-3)
s1.display()
s1.getmini()
print(s1.top())
s1.pop()
print(s1.top())
s1.pop()