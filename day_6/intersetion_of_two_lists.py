# defining a node for LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getcount(head):
    temp=head
    c1=0
    while temp!=None:
        c1=c1+1
        temp=temp.next
    return c1
def getIntersectionNode(head1, head2):
    temp1=head1
    temp2=head2
    c1=getcount(head1)
    c2=getcount(head2)
    if c1>c2:
        for i in range(c1-c2):
            temp1=temp1.next
    if c2>c1:
        for i in range(c2-c1):
            temp2=temp2.next
    while temp1!=None and temp2!=None:
        if temp1==temp2:
            return temp1.data
        temp1=temp1.next
        temp2=temp2.next
    return -1


common = Node(15)
head1 = Node(3)
head1.next = Node(6)
head1.next.next = Node(9)
head1.next.next.next = common
head1.next.next.next.next = Node(30)

# Defining second Li
head2 = Node(10)
head2.next = common
head2.next.next = Node(30)

print("The node of intersection is ", getIntersectionNode(head1, head2))

# The code is contributed by Ansh Gupta.
