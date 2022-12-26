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
    def reverse(self,temp):
        Curr=temp
        Prev=None
        Next=None
        while Curr!=None:
            Next=Curr.next
            Curr.next=Prev
            Prev=Curr
            Curr=Next
        temp=Prev
        return temp

    def palindrome(self):
        if self.head==None and self.head.next==None:
            return True
        slow=self.head
        fast=self.head
        f=0
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        print()

        slow.next=self.reverse(slow.next)
        slow=slow.next
        temp1=self.head
        while slow!=None:
            if temp1.data!=slow.data:
                f=1
                break
            temp1=temp1.next
            slow=slow.next
        if f==1:
            return "Not A Palindrome"
        else:
            return "Palindrome"




llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(3)
llist.push(2)
llist.push(1)

res=llist.palindrome()
print(res)
