from _collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def cycle_detection(self):

        indegree=[0]*self.v
        st=[]

        for i in range(self.v):
            for k in self.graph[i]:
                indegree[k]=indegree[k]+1
        for i in range(self.v):
            if indegree[i]==0:
                st.append(i)
        c=0
        top = []
        while len(st)>0:
            x=st.pop(0)
            top.append(x)
            c=c+1
            for j in self.graph[x]:
                indegree[j]=indegree[j]-1
                if indegree[j] == 0:
                    st.append(j)
        if c == self.v:
            return False
        return True


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
res=g.cycle_detection()
print(res)