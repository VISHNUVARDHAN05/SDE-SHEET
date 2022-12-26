# After Building Co-ordinates Choose First Element
class Node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.data=x

def buildTree(inn, pre, Ins, Ine):
    if Ins>Ine:
        return None
    global mp,preInd
    curr=pre[preInd]
    preInd=preInd+1
    root=Node(curr)
    ind=mp[curr]
    root.left=buildTree(inn,pre,Ins,ind-1)
    root.right = buildTree(inn, pre, ind + 1, Ine)
    return root

def buldTreeWrap(inn, pre, lenn):
    global mp
    for i in range(len(inn)):
        mp[inn[i]]=i
    return buildTree(inn, pre, 0, lenn - 1)

def prInorder(root):
    if root!=None:
        prInorder(root.left)
        print(root.data,end=" ")
        prInorder(root.right)
inn = ['D', 'B', 'E', 'A', 'F', 'C']
pre = ['A', 'B', 'D', 'E', 'C', 'F']
mp={}
preInd=0
lenn = len(inn)

root = buldTreeWrap(inn, pre, lenn)

# Let us test the built tree by printing
# Inorder traversal
print("Inorder traversal of "
      "the constructed tree is")

prInorder(root)