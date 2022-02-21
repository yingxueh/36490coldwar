import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import sys
sys.path.insert(0, '..')
from graph import *
from extract_names import *


import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def getdata(filename):
    docs = []
    file = open(filename, 'r')
    for line in file.readlines():
        docs.append(line)
    print(docs)
    return docs


def baseline_graph(csv, names):
    documents = getdata("baseline.txt")
    write_csv(csv, names, documents)

    df = pd.read_csv(csv)
    mydata = np.genfromtxt(csv, delimiter=',')
    mydata = mydata[1:,1:]

    names = list(df.columns)[1:]

    A = make_adjacency_matrix(mydata, names)
    baselineG = nx_graph_from_adjacency_matrix(A, names)
    return baselineG



if __name__ == "__main__":
    csv = "baseline_frequency.csv"
    names = getlastnames("../names.csv")
    baseline_graph(csv, names)
    