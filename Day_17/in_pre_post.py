# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def in_pre_post(root):
    if root==None:
        return
    else:
        stack=[]
        ino=[]
        pre=[]
        post=[]
        value=0
        stack.append([root,value])
        while len(stack)!=0:
            x=stack.pop()
            if x[1]==0:
                pre.append(x[0].data)
                stack.append([x[0],x[1]+1])
                if x[0].left!=None:
                    stack.append([x[0].left,0])
            if x[1]==1:
                ino.append(x[0].data)
                stack.append([x[0], x[1] + 1])
                if x[0].right!=None:
                    stack.append([x[0].right,0])
            if x[1]==2:
                post.append(x[0].data)

        print(ino)
        print(pre)
        print(post)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
in_pre_post(root)