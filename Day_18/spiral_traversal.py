# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def in_pre_post(root):
    if root==None:
        return -1
    else:
        stack=[]
        stack.append(root)
        f=True
        while len(stack)!=0:
            x=stack.pop(0)
            print(x.data,end=" ")
            if f==True:
                if x.right!=None:
                    stack.append(x.right)
                if x.left!=None:
                    stack.append(x.left)
                f=False
            else:
                if x.left!=None:
                    stack.append(x.left)
                if x.right!=None:
                    stack.append(x.right)
                f=True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
in_pre_post(root)