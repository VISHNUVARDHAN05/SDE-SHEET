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
    def remove(self,n):
        slow=self.head
        fast=self.head
        for i in range(n):
            if fast.next == None:
                if (i == n - 1):
                    self.head = self.head.next
                return self.head
            fast=fast.next

        while fast.next!=None:

            slow=slow.next
            fast=fast.next

        if fast==self.head:
            temp=self.head
            self.head=self.head.next
        else:
            slow.next=slow.next.next




listA = LinkedList()

# Add elements to the list in sorted order

listA.push(1)
listA.push(2)
listA.push(5)
listA.push(20)
listA.push(3)
listA.push(2)
listA.printList()
print()
listA.remove(3)
listA.printList()