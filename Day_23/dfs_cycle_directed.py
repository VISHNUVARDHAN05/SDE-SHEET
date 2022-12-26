from _collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def cycle_detect(self,node,visited,dfs_visited):
        visited[node]=1
        dfs_visited[node]=1
        for i in self.graph[node]:
            if visited[i]==0:
                if self.cycle_detect(i,visited,dfs_visited)==True:
                    return True
            elif visited[i]==1 and dfs_visited[i]==1:
                return True
        dfs_visited[node]=0
        return False

    def dfs(self):
        visited=[0]*(self.v)
        dfs_visited=[0]*(self.v)
        for i in range(self.v):
            if visited[i]==0:
                if self.cycle_detect(i,visited,dfs_visited)==True:
                    return True
        return False
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.dfs() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
