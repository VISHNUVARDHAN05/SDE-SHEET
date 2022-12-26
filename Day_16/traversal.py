class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def pre_post_ino(root):
    if root==None:
        return None
    st=[]
    pre=[]
    pos=[]
    ino=[]
    st.append([root,1])
    while len(st)!=0:
        x=st.pop()
        if x[1]==1:
            pre.append(x[0].data)
            x[1]=x[1]+1
            st.append(x)
            if x[0].left!=None:
                st.append([x[0].left,1])
        elif x[1]==2:
            ino.append(x[0].data)
            x[1] = x[1] + 1
            st.append(x)
            if x[0].right!=None:
                st.append([x[0].left,1])
        else:
            pos.append(x[0].data)

    print(ino)
    print(pre)
    print(pos)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
pre_post_ino(root)