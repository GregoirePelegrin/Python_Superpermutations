from alive_progress import alive_bar
from itertools import permutations
from matplotlib import pyplot as plt

import LibSuperpermutation as sl

def generateGraph(eltss):
	tempGraph = []
	for elts in eltss:
		temp = ""
		for elt in elts:
			temp += elt
		tempGraph.append(sl.Node(temp))
	return tempGraph
def generatePool(nbrElts):
	temp = []
	for i in range(nbrElts):
		temp.append(chr(65+i))
	return temp
# Functions relative to the Nearest Neighbour algorithm
def NearestNeighbour_findNearest(node, nodes):
	minDist = node.distance(nodes[0])
	minIndex = 0
	minNode = nodes[0]
	for i,n in enumerate(nodes):
		d = node.distance(n)
		if minDist > d:
			minDist = d
			minIndex = i
			minNode = n
	return minNode, minIndex
def NearestNeighbour_getBestNearestNeighbour(nodes):
	temp = sl.Superpermutation()
	for n in graph:
		temp.include(n)
	minSuperp = temp
	with alive_bar(len(nodes)) as bar:
		for starter in nodes:
			temp = NearestNeighbour_getCurrentNearestNeighbour(nodes, starter, minSuperp)
			if minSuperp.length > temp.length:
				minSuperp = temp
			bar()
	return minSuperp
def NearestNeighbour_getCurrentNearestNeighbour(nodes, starter, minSuperp):
	nodesList = nodes[:]
	temp = sl.Superpermutation().include(starter)
	currentNode = starter
	while temp.length < minSuperp.length and len(nodesList) != 0:
		nextNode, nextIndex = NearestNeighbour_findNearest(currentNode, nodesList)
		temp.include(nextNode)
		del nodesList[nextIndex]
	return temp

# ORDER = int(input("Number of elts: "))

minLengths = []
for ORDER in range(1, 7):
	# Generate the pool of elts from the number of elt
	pool = generatePool(ORDER)
	permutationList = list(permutations(pool))
	graph = generateGraph(permutationList)

	# Implementing Nearest-Neighbour on the graph
	superpermutation = NearestNeighbour_getBestNearestNeighbour(graph)
	minLengths.append(superpermutation.length)

x = [i for i in range(1, 7)]
yTheo = [1, 3, 9, 33, 153, 872]
plt.plot(x, yTheo, label="Theoretical lengths")
plt.plot(x, minLengths, label="Nearest-Neighbour")
plt.legend()
plt.show()