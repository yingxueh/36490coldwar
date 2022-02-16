from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def make_adjacency_matrix(M, names):
    n = len(names)
    print(M.shape, n)
    A = np.zeros(n * n)
    A = A.reshape((n,n))
    print(A.shape)
    for doc in M:
        for i in range(n):
            if doc[i] != 0:
                for j in range(i+1, len(doc)):
                    if doc[j] != 0:
                        A[i][j] += 1
                        A[j][i] += 1
    print(A)
    return A


def nx_graph_from_adjacency_matrix(M, names):
    print(M.shape)
    V = names
    print(len(V))

    # Create the graph and add each set of nodes
    G = nx.Graph()
    G.add_nodes_from(V, nodetype="green")

    # Find the non-zero indices in the biadjacency matrix to connect those nodes
    G.add_edges_from([ (V[i], V[j]) for i, j in zip(*M.nonzero()) ])
    
    # remove isolated nodes
    deg = G.degree()
    to_remove = [n[0] for n in deg if n[1] == 0]
    G.remove_nodes_from(to_remove)
    
    # formatting
    nx.draw(G, font_size=5, node_size=7, with_labels=True)
    plt.show()
    return G

# makes bipartite graph from documents to people
def nx_graph_from_biadjacency_matrix(M, txtfiles, names):
    print(M.shape)

    U = txtfiles
    V = names
    print(len(U), len(V))

    # Create the graph and add each set of nodes
    G = nx.Graph()
    G.add_nodes_from(U, bipartite=0, nodetype="grey", nodesize=300, nodelabel=False)
    G.add_nodes_from(V, bipartite=1, nodetype="blue", nodesize=50, nodelabel=True)

    # Find the non-zero indices in the biadjacency matrix to connect those nodes
    G.add_edges_from([ (U[i], V[j]) for i, j in zip(*M.nonzero()) ])
    
    # remove isolated nodes
    deg = G.degree()
    to_remove = [n[0] for n in deg if n[1] == 0]
    G.remove_nodes_from(to_remove)
    
    # formatting
    colors = [u[1] for u in G.nodes(data="nodetype")]
    sizes = [u[1] for u in G.nodes(data="nodesize")]
    labels = [u[1] for u in G.nodes(data="nodelabel")]
    pos = nx.spring_layout(G, seed=101)
    nx.draw(G, pos=pos, node_size = sizes, with_labels=False, node_color = colors, edgecolors='black')

    print(pos)
    textPos = pos.copy()
    for k in textPos:
        textPos[k][1] -= .035
        pass

    labels = {}    
    for node in G.nodes():
        if ".txt" not in node:
            #set the node name as the key and the label as its value 
            labels[node] = node
    nx.draw_networkx_labels(G, textPos, labels, font_size=8, font_family="arial")

    plt.show()
    return G


if __name__ == "__main__":
    filename = 'frequency.csv'
    df = pd.read_csv(filename)
    mydata = genfromtxt(filename, delimiter=',')
    mydata = mydata[1:,1:]

    names = list(df.columns)[1:]
    txtfiles = list(df["id"])

    # nx_graph_from_biadjacency_matrix(mydata, txtfiles, names)

    A = make_adjacency_matrix(mydata, names)
    #nx_graph_from_adjacency_matrix(A, names)
    nx_graph_from_biadjacency_matrix(mydata, txtfiles, names)



