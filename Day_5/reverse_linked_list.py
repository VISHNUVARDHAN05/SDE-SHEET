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
    def reverse(self):
        Curr=self.head
        Prev=None
        Next=None
        while Curr!=None:
            Next=Curr.next
            Curr.next=Prev
            Prev=Curr
            Curr=Next
        self.head=Prev


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print
"Given Linked List"

llist.reverse()
print
"\nReversed Linked List"
llist.printList()
