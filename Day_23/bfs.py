from _collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,v):
        visited={}
        bfs=[]
        for i in range(1,v+1):
            if i not in visited:
                stack=[]
                stack.append(i)
                visited[i]=True
                while len(stack)>0:
                    x=stack.pop(0)
                    bfs.append(x)
                    for k in self.graph[x]:
                        if k not in visited:
                            stack.append(k)
                            visited[k]=True
        print(bfs)

