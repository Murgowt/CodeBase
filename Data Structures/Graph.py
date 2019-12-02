#Implemented using an Adjacency Graph Concept.
class graph:
    def __init__(self):
        self.vertices=int(input("Enter number of Vertices: "))
        self.adj=[]
        for i in range(self.vertices):
            temp=[0 for j in range(self.vertices)]
            self.adj.append(temp)
    def add_edge(self):
        Vpair=list(map(int,input("Enter the Vertices(Space Seperated): ").split()))
        self.adj[Vpair[0]][Vpair[1]]=1
        self.adj[Vpair[1]][Vpair[0]]=1
    def print_edges(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj[i][j]==1:
                    print("{}--{}".format(i,j))
G=graph()
G.add_edge()
G.add_edge()
G.add_edge()
G.print_edges()
print("All OK")

