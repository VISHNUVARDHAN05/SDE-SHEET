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



def mergeLists(l1,l2):
    if l1==None:
        return l2
    if l2==None:
        return l1

    if l1.data>l2.data:
        #print(l1.data,l2.data)
        temp=l1
        l1=l2
        l2=temp
    res=l1
    while l1!=None and l2!=None:
        temp=Node(None)
        while l1!=None and l1.data<=l2.data:
            temp=l1
            l1=l1.next
        temp.next=l2
        l1,l2=l2,l1

    return res
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order

listA.push(25)
listA.push(10)
listA.push(5)


listB.push(20)
listB.push(3)
listB.push(2)

listA.head = mergeLists(listA.head, listB.head)
# Display merged list
print("Merged Linked List is:")
listA.printList()
