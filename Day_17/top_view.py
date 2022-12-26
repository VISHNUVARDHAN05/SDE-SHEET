# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def top_view(root):
    if root==None:
        return
    else:
        level=0
        stack=[]
        d={}
        stack.append([root,level])
        while len(stack)!=0:
            x=stack.pop(0)
            if x[1] in d:
                d[x[1]].append(x[0].data)
            else:
                d[x[1]]=[x[0].data]
            if x[0].left!=None:
                stack.append([x[0].left,x[1]-1])
            if x[0].right!=None:
                stack.append([x[0].right,x[1]+1])
    for k ,v in enumerate(sorted(d)):
        x=d[v]
        print(k,x[0])




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
top_view(root)