# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def morris_inorder(node):
    curr=node
    ino=[]
    while curr!=None:
        if curr.left==None:
            ino.append(curr.data)
            curr=curr.right
        else:
            x=curr.left
            while x.right!=None and x.right!=curr:
                x=x.right
            if x.right==None:
                x.right=curr
                curr=curr.left
            else:
                x.right=None
                ino.append(curr.data)
                curr=curr.right

    print(ino)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
morris_inorder(root)
