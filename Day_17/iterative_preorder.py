class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def preorder(root):
    if root==None:
        return None
    st=[]
    pre=[]
    st.append(root)
    while len(st)!=0:
        x=st.pop()
        pre.append(x.data)
        if x.right != None:
            st.append(x.right)
        if x.left!=None:
            st.append(x.left)


    print(pre)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
preorder(root)