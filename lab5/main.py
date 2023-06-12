import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


header_list = ["Node-1","Node-2","weight"]
E = pd.read_csv('./insecta-ant-colony1-day10.edges',sep=" ", names=header_list)
G = nx.from_pandas_edgelist(E,'Node-1',"Node-2",["weight"])
nx.draw(G)
plt.show()

V = G.number_of_nodes()
E = G.number_of_edges()
print(f"the no. of vertices of the graph is: {V}")
print(f"the no. of edges of the graph is: {E}")

def density(G):
    V = G.number_of_nodes()
    E = G.number_of_edges()
    if(abs(V) > 1 ):
        return 2*abs(E)/( abs(V)*(abs(V)-1))
    else:
        return 0
D = density(G)
print(f"the desity of graph is {D}")

average_degree = sum(dict(G.degree()).values()) / len(G)
print(f"The average degree is {average_degree}")

def bfs(G, start):
        visited = {}        
        distance = {}
        queue = []

        queue.append(start)
        visited[start] = True
        distance[start] = 0

        while queue:
            m = queue.pop(0)
            for i in G.neighbors(m):
                if i not in visited:
                    queue.append(i)
                    visited[i] = True
                    distance[i] = distance[m] + 1

        return max(distance.values())

def diameter(G):
    diameter = 0
    for node in G.nodes:
        diameter = max(diameter,bfs(G, node))
    return diameter

print(f"The diameter is {diameter(G)}")
# print(f"The diameter is {nx.diameter(G)}")


def cluster(Graph , node):
    cc = 0
    ki = Graph.degree(node) # degree of the node vertex
    neighbors = list(Graph.neighbors(node)) # neighbour vertices of node
    ei = 0 # no of links between the neighbours
    for i in range(len(neighbors)):
        for j in range(i+1, len(neighbors)):
            if Graph.has_edge(neighbors[i], neighbors[j]):
                ei += 1
    if ki >1:
        cc = 2*ei/(ki*(ki-1))
    elif ki == 0:
        cc = 0
    return cc

            

def Clustering_coefficient(Graph):
    cluster_sum = 0
    for  node in Graph.nodes():
        temp = cluster(Graph,node)
        cluster_sum = cluster_sum + temp 
    cluster_sum = cluster_sum / Graph.number_of_nodes()
    return cluster_sum

cl = Clustering_coefficient(G)
print(f"the Clustering coeffient is found to be{cl}")


# Calculate the degree distribution
degree_counts = nx.degree_histogram(G)
degrees = range(len(degree_counts))
plt.plot(degrees, degree_counts, marker='o', linestyle='-', color='g')
plt.xlabel("Degree")
plt.ylabel("Count")
plt.title("Degree Distribution (Point Plot)")
plt.show()
  