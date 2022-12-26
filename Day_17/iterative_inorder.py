class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x


def preorder(node):

    if node==None:
        return None
    st=[]
    ino=[]
    while True:
        if node!=None:
            st.append(node)
            node=node.left
        else:
            if len(st)==0:
                break
            node=st.pop()
            ino.append(node.data)
            node=node.right

    print(ino)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
preorder(root)