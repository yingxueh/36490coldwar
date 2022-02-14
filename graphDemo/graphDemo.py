import networkx as nx
import nxviz as nv
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

class Network():
	def __init__(self, corpa : list):
		self.corpa = corpa
		self.names = self.populateNames()  # dict { alias : name }
		self.graph = nx.Graph()

	def populateNames(self):
		# read in names.csv
		# populate self.names with all the people
		# for now, just set all entries as {alias : alias}
		pass


	def makeGraph(self):
		# for document in self.corpa:
		#     for name1 in grabNames(document):
		#         for name2 in grabBames(document)[-name1]:
		#              self.handleEdge(name1, name2)
		pass

	def grabNames(self, document : str) -> list:
		# fuzzy matching?
		# return a list of all the names that appear in the document
		pass

	def handleEdge(self, person1 : str, person2 : str):
		# if self.graph.has_edge(person1, person2):
		#	self.graph[name1][name2]['weight'] += 1
		# else:
		# 	self.graph.add_edge(name1, name2, weight=1)
		pass


def main():
	print("hey")

main()