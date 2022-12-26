# After Building Co-ordinates Choose First fElement

class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x

def lca(node,n1,n2):
    if node==None or node.data==n1 or node.data==n2:
        return node
    lh=lca(node.left,n1,n2)
    rh=lca(node.right,n1,n2)
    if lh==None:
        return rh
    elif rh==None:
        return lh
    else:
        return node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
maxi=lca(root,4,5)
print(maxi.data)