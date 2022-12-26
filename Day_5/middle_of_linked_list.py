class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp=self.head
        while temp!=None:
            print(temp.data,sep=" ",end=" ")
            temp=temp.next
    def middle(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)

llist = LinkedList()
for i in range(5, 0, -1):
    llist.push(i)
llist.middle()