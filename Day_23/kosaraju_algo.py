from _collections import defaultdict
class Graph:
    def __init__(self,ver):
        self.v=ver
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,transpose_graph,x,visited):
        visited[x]=1
        print(x,end=" ")
        for adj in transpose_graph[x]:
            if visited[adj]==0:
                self.dfs(transpose_graph, adj, visited)


    def topsort(self,node, visited,res):
        visited[node]=1
        for adj in self.graph[node]:
            if visited[adj]==0:
                self.topsort(adj, visited, res)
        res.append(node)
    def transpose_graph(self):
        temp=defaultdict(list)
        for i in range(self.v):
            for j in self.graph[i]:
                temp[j].append(i)
        return temp

    def kosaraju_algo(self):
        visited=[0]*self.v
        res=[]
        stack=[]
        for i in range(self.v):
            if visited[i]==0:
                self.topsort(i,visited,res)
        transpose_graph=self.transpose_graph()
        visited = [0] * self.v
        while len(res)>0:
            x=res.pop()
            if visited[x]==0:
                self.dfs(transpose_graph,x,visited)
                print()

'''
# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.kosaraju_algo()
'''
g= Graph(7)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4,5)
g.addEdge(6,5)
g.addEdge(3,6)
g.addEdge(5,3)
g.kosaraju_algo()


'''
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.kosaraju_algo()
'''