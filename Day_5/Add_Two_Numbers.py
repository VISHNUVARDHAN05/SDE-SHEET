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





def Add_Two_Numbers(listA,listB):
    if listA==None:
        return listA
    if listB==None:
        return listB
    res=LinkedList()
    carry=0
    sum1=0
    l1=listA.head
    l2=listB.head
    while l1!=None and l1!=None:
        sum1=l1.data+l2.data+carry
        if sum1<10:
            res.push(sum1)
        else:
            res.push(sum1%10)
            carry=sum1//10
        l1= l1.next
        l2=l2.next
    while l1!=None:
        res.push(l1.data)
        l1=l1.next
    while l2!=None:
        res.push(l1.data)
        l2=l2.next

    return res
listA = LinkedList()
listB=LinkedList()
# Add elements to the list in sorted order

listA.push(1)
listA.push(2)
listA.push(3)
listB.push(3)
listB.push(2)
listB.push(1)
listA.printList()
print()
listB.printList()
print()
listA.reverse()
listB.reverse()
res=Add_Two_Numbers(listA,listB)
res.printList()
print()
#listA.printList()