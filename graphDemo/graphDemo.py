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
		# populate self.names with all the people, where the key is their alias
		# and the value is the primary key/ consistant value we'll use in our visualization
		# Purpose: handles people that go by multiple names/ titles in the documents
		# EXAMPLE:
		# { John Doe : John Doe
		#  Dwight Eisenhower : Dwight Eisenhower
		#  Eisenhower : Dwight Eisenhower
		#  Mr. President : Dwight Eisenhower
		#  President Eisenhower : Dwight Eisenhower}
		pass


	def makeGraph(self):
		# for document in self.corpa:
		#     for name1 in grabNames(document):
		#         for name2 in grabBames(document)[-name1]:
		#              self.handleEdge(name1, name2)
		pass

	def grabNames(self, freqs) -> list:
		# fuzzy matching?
		# return a list of all the names that appear in the document

		# names = []
		# for row in frequencies.csv:
		# 	for col in row:
		#       if df[row][col] > 1:
		#           names.append(df[row][col].name (I forget the exact pandas syntax))
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