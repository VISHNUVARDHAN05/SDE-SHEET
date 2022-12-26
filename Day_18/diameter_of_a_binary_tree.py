# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def diameter(node,maxi):
    if node==None:
        return 0

    lh=diameter(node.left,maxi)
    rh=diameter(node.right,maxi)
    maxi[0] = max(maxi[0], 1+lh + rh)
    return 1+max(lh,rh)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
maxi=[0]
diameter(root,maxi)
print(maxi)