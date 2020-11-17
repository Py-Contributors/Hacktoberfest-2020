from collections import defaultdict 
class Graph: 
    def __init__(self):  
        self.graph = defaultdict(list) 
        
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) #undirected graph
    
    def depth(self, v, visited): 
        visited[v] = True
        print(v, end = ' ') 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.depth(i, visited) 
    
    def DFSAlgorithm(self, v): 
        visited = [False] * (max(self.graph)+1) 
        self.depth(v, visited)

gObj = Graph()
gObj.addEdge(0,3)
gObj.addEdge(0,2)
gObj.addEdge(0,4)
gObj.addEdge(3,5)
gObj.addEdge(3,7)
gObj.addEdge(7,5)
gObj.addEdge(1,2)
gObj.addEdge(1,6)
gObj.addEdge(6,2)
gObj.addEdge(6,4)
gObj.DFSAlgorithm(0)
print("\n",gObj.graph)