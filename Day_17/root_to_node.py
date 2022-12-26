# After Building Co-ordinates Choose Last Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def root_to_node(node,val,arr):
    if node==None:
        return False
    arr.append(node.data)
    if node.data==val:
        return True
    if root_to_node(node.left,val,arr) or root_to_node(node.right,val,arr):
        return True
    arr.pop()
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print ("Vertical order traversal is")
arr=[]
root_to_node(root,8,arr)
print(arr)