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

    def detect_loop_linked_list(self):
        slow=self.head
        fast=self.head
        while slow!=None and fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=self.head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                    if slow==fast:
                        return slow.data
                return False
        return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head
res=llist.detect_loop_linked_list()
print(res)