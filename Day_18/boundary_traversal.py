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
def boundary_traversal(node):
    if node==None:
        return -1

    print(node.data,end=" ")
    printleft(node.left)
    printleaves(node)
    printright(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
boundary_traversal(root)