class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def get_parent(node,k):
    stack=[]
    parent_map={}
    res=None
    stack.append(node)
    while len(stack)!=0:
        x=stack.pop(0)
        if x.data==k:
            res=x
        if x.left!=None:
            parent_map[x.left]=x
            stack.append(x.left)
        if x.right!=None:
            parent_map[x.right]=x
            stack.append(x.right)
    return parent_map,res

def min_time(node,k):
    if node==None:
        return 0
    else:
        parent_map,k_node=get_parent(node,k)
        c=0
        stack=[]
        stack.append(k_node)
        visited={}
        visited[k_node]=True
        while len(stack)!=0:
            l=len(stack)
            f=0
            for i in range(l):
                x = stack.pop(0)
                if x.left!=None and x.left not in visited:
                    visited[x.left]=True
                    f= 1
                    stack.append(x.left)
                if x.right!=None and x.right not in visited:
                    visited[x.right]=True
                    f=1
                    stack.append(x.right)
                if x in parent_map and parent_map[x] not in visited:
                    visited[parent_map[x]]=True
                    f=1
                    stack.append(parent_map[x])
            if f==1:
                c=c+1
    return c


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)
res=min_time(root,4)
print(res)