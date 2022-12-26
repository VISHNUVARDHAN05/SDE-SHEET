# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def printleaves(node):
    if node!=None:
        printleaves(node.left)
        if node.left==None and node.right==None:
            print(node.data,end=" ")
        printleaves(node.right)
def printleft(node):
    if node:
        if node.left:
            print(node.data,end=" ")
            printleft(node.left)
        elif node.right:
            print(node.data,end=" ")
            printleft(node.right)
def printright(node):
    if node:
        if node.right:
            print(node.data,end=" ")
            printleft(node.right)
        elif node.left:
            print(node.data,end=" ")
            printleft(node.left)
def max_path_sum(node,maxi):
    if node==None:
        return 0
    lh=max(0,max_path_sum(node.left,maxi))
    rh=max(0,max_path_sum(node.right,maxi))
    maxi[0]=max(maxi[0],lh+rh+node.data)
    return node.data+max(lh,rh)


root = Node(10)
root.left = Node(2)
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)
maxi=[0]
max_path_sum(root,maxi)
print(maxi)