class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def right_view(root,level,stack):
    if root==None:
        return
    if level==len(stack):
        stack.append(root.data)

    right_view(root.right,level+1,stack)
    right_view(root.left,level+1,stack)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
stack=[]
right_view(root,0,stack)
print(stack)