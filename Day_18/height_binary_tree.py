# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def height(node):
    if node==None:
        return 0
    lh=height(node.left)
    rh=height(node.right)
    return 1+max(lh,rh)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
x=height(root)
print(x)