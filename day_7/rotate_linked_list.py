class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,sep=" ")
            temp=temp.next

    def rotate_linked_list(self,k):
        if k==0 or self.head==None or self.head.next==None:
            return self.head
        c=1
        temp=self.head
        while temp.next!=None:
            c=c+1
            temp=temp.next
        k=k%c
        k=c-k
        temp.next=self.head
        for i in range(k):
            temp=temp.next

        self.head=temp.next
        temp.next=None
        return self.head

#1->2->3->4->5
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
#llist.display()
print()
llist.head=llist.rotate_linked_list(2)
llist.display()
