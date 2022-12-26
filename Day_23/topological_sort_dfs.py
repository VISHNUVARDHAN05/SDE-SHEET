from _collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,node,visited,res):
        visited[node]=1
        for i in self.graph[node]:
            if visited[i]==0:
                self.dfs(i,visited,res)
        res.append(node)

    def topological_sort(self):
        visited=[0]*(self.v)
        res=[]
        for i in range(self.v):
            if visited[i]==0:
                self.dfs(i,visited,res)
        res=res[::-1]
        print(res)
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topological_sort()