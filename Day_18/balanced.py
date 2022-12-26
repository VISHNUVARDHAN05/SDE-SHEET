# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def diameter(node):
    if node==None:
        return 0
    lh=diameter(node.left)
    if lh==-1:
        return -1
    rh=diameter(node.right)
    if rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    return 1+max(lh,rh)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
maxi=diameter(root)
if maxi==-1:
    print("False")
else:
    print("True")