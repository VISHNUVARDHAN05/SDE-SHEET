from _collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfsutil(self,node, visited,res):
        visited[node]=True
        res.append(node)
        for key in self.graph[node]:
            if key not in visited:
                self.dfsutil(key,visited,res)

    def dfs(self,v):
        visited={}
        res=[]
        for i in range(1,visited+1):
            if i not in visited:
                self.dfsutil(i,visited,res)
        print(res)

