from collections import defaultdict

class Graph:
    """ Graph with V vertices """
    def __init__(self,V):
        self.V = V
        self.adjList = defaultdict(list)
    
    def addEdge(self,src,dest):
        """ Directed graph """
        if src <= self.V and dest <= self.V:
            self.adjList[src].extend([dest])

    def bfs(self, node):
        visited = [False]*(self.V)
        Q = []
        Q.append(node)
        visited[node-1] = True
        while Q:
            tmp = Q.pop(0)
            print(tmp)
            for n in self.adjList[tmp]:
                if visited[n-1] is False:
                    Q.append(n)
                    visited[n-1] = True

    def dfs(self,src):
        visited = [False] * (self.V)
        st = []
        st.append(src)
        visited[src-1] = True

        while st:
            curr_v = st.pop()
            print(curr_v)
            for adj_v in self.adjList[curr_v]:
                if not visited[adj_v-1]:
                    st.append(adj_v)
                    visited[adj_v - 1] = True


#main

g = Graph(4)
g.addEdge(4,3)
g.addEdge(3,1)
g.addEdge(2,1)
g.addEdge(1,2)
g.addEdge(2,4)
g.bfs(2)
