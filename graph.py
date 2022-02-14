from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    # nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    nx.draw(gr)
    plt.show()

def nx_graph_from_biadjacency_matrix(M, txtfiles, names):
    # Give names to the nodes in the two node sets
    print(M.shape)

    U = txtfiles
    V = names
    print(len(U), len(V))

    # Create the graph and add each set of nodes
    G = nx.Graph()
    G.add_nodes_from(U, bipartite=0, nodetype="yellow")
    G.add_nodes_from(V, bipartite=1, nodetype="green")

    # Find the non-zero indices in the biadjacency matrix to connect 
    # those nodes
    G.add_edges_from([ (U[i], V[j]) for i, j in zip(*M.nonzero()) ])
    
    # remove isolated nodes
    deg = G.degree()
    to_remove = [n[0] for n in deg if n[1] == 0]
    G.remove_nodes_from(to_remove)
    
    colors = [u[1] for u in G.nodes(data="nodetype")]
    nx.draw(G, font_size=5, node_size=7, with_labels=True, node_color = colors)
    plt.show()
    return G


if __name__ == "__main__":
    filename = 'frequency.csv'
    df = pd.read_csv(filename)
    mydata = genfromtxt(filename, delimiter=',')
    mydata = mydata[1:,1:]
    names = list(df.columns)[1:]
    print(names)
    txtfiles = list(df["id"])
    print(txtfiles)
    # show_graph_with_labels(adjacency, None)
    nx_graph_from_biadjacency_matrix(mydata, txtfiles, names)

