import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import sys
sys.path.insert(0, '..')
from graph import *
from frequency import *


import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def getdata(filename):
    docs = []
    file = open(filename, 'r')
    for line in file.readlines():
        docs.append(line)
    return docs


def base_freq(csv, names):
    documents = getdata("baseline.txt")
    write_csv(csv, names, documents)

if __name__ == "__main__":
    csv = "baseline_frequency.csv"
    names = getlastnames("../names.csv")
    base_freq(csv, names)
    