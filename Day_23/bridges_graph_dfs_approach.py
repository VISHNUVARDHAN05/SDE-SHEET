from collections import defaultdict

class Graph:
    def __init__(self,ver):
        self.v=ver
        self.graph=defaultdict(list)
        self.time=0
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DfsUtil(self,node,visited,low,time,parent):
        visited[node]=1
        low[node]=self.time
        time[node]=self.time
        self.time=self.time+1
        for adj in self.graph[node]:
            if visited[adj]==0:
                parent[adj]=node
                self.DfsUtil(adj,visited,low,time,parent)
                low[node]=min(low[node],low[adj])
                if low[adj]>time[node]:
                    print(adj,node)
            elif adj!=parent[node]:
                low[node]=min(low[node],time[adj])





    def bridges_graph(self):
        visited=[0]*self.v
        low=[0]*self.v
        time = [0] * self.v
        parent=[-1]*self.v
        for i in range(self.v):
            if visited[i]==0:
                self.DfsUtil(i,visited,low,time,parent)


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print("Bridges in first graph ")
g1.bridges_graph()