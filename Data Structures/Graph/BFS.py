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
                print(self.adj[i][j],end=" ")
            print(self.adj[i][j])
    def BFS(self):
    	visited=[False  for  sv in range(self.vertices)]
    	queue=[]
    	output=[]
    	front,rear=0,0
    	queue.append(0)
    	for j  in range(self.vertices):
    		if(self.adj[0][j]==1):
    			queue.append(j)
    			visited[j]=True
    			rear+=1
    			if(front==0):
    				front+=1
    	visited[0]=True
    	output.append(0)
    	while(front!=rear):
    		f=queue[front]
    		
    		for ver in range(self.vertices):
    			if(self.adj[f][ver]==1):
    				if(not visited[ver]):
    					queue.append(ver)
    					visited[ver]=True
    					rear+=1
    			print("queue:",queue,"at f: ",f)
    		output.append(f)
    		front+=1
    	output.append(queue[front])
    	print("The BFS Traversal of the Graph is: ",end=" ")
    	for i in output:
    		print(i,end=" ")


G=graph()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.add_edge()
G.print_edges()
G.BFS()
print("All OK")