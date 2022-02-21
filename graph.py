from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import sys

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
np.set_printoptions(threshold=sys.maxsize)

def getfreqmatrix(filename):
    df = pd.read_csv(filename)
    names = list(df.columns)[1:]
    rownames = list(df["id"])  
    mydata = genfromtxt(filename, delimiter=',')
    mydata = mydata[1:,1:]
    return (names, rownames, mydata)


# M is a frequency matrix rows=documents, columns=names
def make_adjacency_matrix(M, names):
    n = len(names)
    print("docs by names", M.shape, n)
    A = np.zeros(n * n).reshape((n,n))
    for doc in M:
        for i in range(n):
            if doc[i] != 0:
                for j in range(i+1, len(doc)):
                    if doc[j] != 0:
                        A[i][j] += 1
                        A[j][i] += 1
    return A

# graph from adjacency matrix names by names
def nx_graph_from_adjacency_matrix(M, names, df):
    V = names

    # Create the graph and add each set of nodes
    G = nx.Graph()
    G.add_nodes_from(V, nodetype="green")

    # Find the non-zero indices in the biadjacency matrix to connect those nodes
    G.add_edges_from([ (V[i], V[j]) for i, j in zip(*M.nonzero()) ])
    
    # remove isolated nodes
    deg = G.degree()
    to_remove = [n[0] for n in deg if n[1] == 0]
    G.remove_nodes_from(to_remove)

    #colors = [float(G.degree(n)) for n in G]
    sizes = [float(G.degree(n))*5 for n in G] 
    labels = {}
    for n in G.nodes():
        if G.degree(n) > 0:
            s = n[0].upper() + n[1:]
            labels[n] = s

    colors = []
    for n in G:
        r = df.loc[df["lastname"].str.lower() == n]
        if r.iloc[0]['affiliation'] == "west":
            colors.append("blue")
        elif r.iloc[0]['affiliation'] == "east":
            colors.append("red")
        else:
            colors.append("grey")
        pass
    
    # formatting
    pos = nx.spring_layout(G, seed=101, k=0.2, iterations=35)

    nx.draw(G, pos=pos, node_color=colors, node_size=sizes, with_labels=False)
    nx.draw_networkx_labels(G, pos, labels, font_size=5, 
            font_weight="bold", verticalalignment="bottom")
    plt.show()
    return G

# Adjust appearance of the nodes, edges, labels, etc.
def adjust_appearance_bipartite(G, pos):
    # Shift labels up off of their node
    textPos = pos.copy()
    for k in textPos:
        textPos[k][1] += .01

    labels = {}    
    for n in G.nodes():
        # Dont label documents, and only label figures with
        # a decently high degree 
        if ".txt" not in n and G.degree(n) > 2:
            s = n[0].upper() + n[1:]
            labels[n] = s
    nx.draw_networkx_labels(G, textPos, labels, font_size=10,  font_weight="bold",
                            verticalalignment="bottom")


# makes bipartite graph from documents to people
def nx_graph_from_biadjacency_matrix(M, txtfiles, names):

    U = txtfiles
    V = names

    # Create the graph and add each set of nodes
    G = nx.Graph()
    G.add_nodes_from(U, bipartite=0, nodetype="doc", nodesize=200, nodelabel=False)
    G.add_nodes_from(V, bipartite=1, nodetype="person", nodesize=50, nodelabel=True)

    # Find the non-zero indices in the biadjacency matrix to connect those nodes
    G.add_edges_from([ (U[i], V[j]) for i, j in zip(*M.nonzero()) ])
    
    # remove isolated nodes
    deg = G.degree()
    to_remove = [n[0] for n in deg if n[1] == 0]
    G.remove_nodes_from(to_remove)

    # Sets the colors of the nodes
    types= G.nodes(data="nodetype")
    print(types)
    colors = []
    for elm in types:
        print(elm)
        (n, typ) = elm
        degree = G.degree(n)
        if typ == "person":
            colors.append(float(degree))
        else:
            colors.append(-10.0)
    
    # formatting
    #colors = [float(G.degree(n)) for n in G]
    sizes = [u[1] for u in G.nodes(data="nodesize")]
    pos = nx.spring_layout(G, seed=101, k=0.1, iterations=15)
    nx.draw(G, pos=pos, node_size = sizes, with_labels=False, node_color = colors, edgecolors='black')

    adjust_appearance_bipartite(G, pos)

    plt.show()
    return G


# given two graphs, returns jaccard index
def get_jaccard_index(G, H):
    A = set(G.edges)
    B = set(H.edges)
    n11 = A.intersection(B)
    n01 = A.difference(B)
    n10 = B.difference(A)
    return len(n11) / (len(n11) + len(n01) + len(n10))


if __name__ == "__main__":
    (names, txtfiles, mydata) = getfreqmatrix("frequency.csv")

    namesdf = pd.read_csv("names.csv")
    A = make_adjacency_matrix(mydata, names)
    G = nx_graph_from_adjacency_matrix(A, names, namesdf)
    # nx_graph_from_biadjacency_matrix(mydata, txtfiles, names)

    (names, ids, basedata) = getfreqmatrix("baseline/baseline_frequency.csv")
    basemat = make_adjacency_matrix(basedata, names)
    baseG = nx_graph_from_adjacency_matrix(basemat, names, namesdf)

    J = get_jaccard_index(G, baseG)
    print("Jaccard index: ", J)