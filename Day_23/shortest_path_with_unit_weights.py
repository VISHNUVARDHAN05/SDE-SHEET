from _collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def min_cost(self,src):
        dist=[32768]*self.v
        dist[src]=0
        st=[]
        st.append(src)
        while len(st)>0:
            x=st.pop(0)
            for i in self.graph[x]:
                if dist[x]+1<dist[i]:
                    dist[i]=dist[x]+1
                    st.append(i)
        print(dist)

g=Graph(9)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,6)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,7)
g.addEdge(6,8)
g.addEdge(7,8)
g.min_cost(0)
