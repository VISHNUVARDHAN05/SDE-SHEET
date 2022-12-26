class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
def left_height(node):
    c=1
    while node!=None:
        c=c+1
        node=node.left
    return c
def right_height(node):
    c=1
    while node!=None:
        c=c+1
        node=node.right
    return c

def TotalNodes(node):
    if node==None:
        return 0
    lh=left_height(node.left)
    rh=right_height(node.right)
    if lh==rh:
        return (2**lh)-1
    return 1+TotalNodes(node.left)+TotalNodes(node.right)
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)

print(TotalNodes(root))