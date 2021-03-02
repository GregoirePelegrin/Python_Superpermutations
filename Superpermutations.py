from alive_progress import alive_bar
from itertools import permutations
from matplotlib import pyplot as plt
from sympy.ntheory import binomial_coefficients

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
def generateSuperpermutationFromGroup(group):
	res = sl.Superpermutation()
	for n in group:
		res.include(n)
	return res
# Functions relative to the Nearest Insertion algorithm
def NearestInsertion_findNearest(group, nodes):	# Not opti: doesn't take into account the direction of the proximity
	minDist = group[0].distance(nodes[0])
	minIndex = 0
	minNode = nodes[0]
	placeIndex = 1
	for i1,n1 in enumerate(group):
		for i2,n2 in enumerate(nodes):
			d = n1.distance(n2)
			if minDist > d:
				minDist = d
				minIndex = i2
				minNode = n2
				placeIndex = i1+1
	return minNode, minIndex, placeIndex
def NearestInsertion_getBestNearestInsertion(nodes):
	temp = sl.Superpermutation()
	if len(nodes) < 2:
		return temp
	for n in nodes:
		temp.include(n)
	minSuperp = temp
	with alive_bar(binomial_coefficients(len(nodes))[(2, len(nodes)-2)], title="NearestInsertion", length=20) as bar:
		for i in range(len(nodes)-1):
			for j in range(i+1, len(nodes)):
				temp = NearestInsertion_getCurrentNearestInsertion(nodes, [nodes[i], nodes[j]], minSuperp)
				if minSuperp.length > temp.length:
					minSuperp = temp
				bar()
	return minSuperp
def NearestInsertion_getCurrentNearestInsertion(nodes, starters, minSuperp):
	nodesList = nodes[:]
	group = starters[:]
	temp = generateSuperpermutationFromGroup(group)
	while temp.length < minSuperp.length and len(nodesList) != 0:
		nextNode, nextIndex, nextPlace = NearestInsertion_findNearest(group, nodesList)
		group.insert(nextPlace, nextNode)
		temp = generateSuperpermutationFromGroup(group)
		del nodesList[nextIndex]
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
	for n in nodes:
		temp.include(n)
	minSuperp = temp
	with alive_bar(len(nodes), title="NearestNeighbour", length=20) as bar:
		for starter in nodes:
			temp = NearestNeighbour_getCurrentNearestNeighbour(nodes, starter, minSuperp)
			if minSuperp.length > temp.length:
				minSuperp = temp
			bar()
	return minSuperp
def NearestNeighbour_getCurrentNearestNeighbour(nodes, starter, minSuperp):
	nodesList = nodes[:]
	currentNode = starter
	temp = sl.Superpermutation().include(currentNode)
	while temp.length < minSuperp.length and len(nodesList) != 0:
		nextNode, nextIndex = NearestNeighbour_findNearest(currentNode, nodesList)
		temp.include(nextNode)
		del nodesList[nextIndex]
	return temp

def comparison(maxOrder=5):
	minLengths = {}
	for ORDER in range(1, maxOrder+1):
		print("ORDER = {}".format(ORDER))
		# Generate the pool of elts from the number of elt
		pool = generatePool(ORDER)
		permutationList = list(permutations(pool))
		graph = generateGraph(permutationList)

		# Implementing Nearest-Neighbour on the graph
		superpermutation = NearestNeighbour_getBestNearestNeighbour(graph[:])
		if "NearestNeighbour" not in minLengths:
			minLengths["NearestNeighbour"] = []
		minLengths["NearestNeighbour"].append(superpermutation.length)

		# Implementing Nearest-Insertion on the graph
		superpermutation = NearestInsertion_getBestNearestInsertion(graph[:])
		if "NearestInsertion" not in minLengths:
			minLengths["NearestInsertion"] = []
		minLengths["NearestInsertion"].append(superpermutation.length)
	return minLengths

n = int(input("To what order? (1-7): "))
x = [i for i in range(1, n)]
yTheo = [1, 3, 9, 33, 153, 872, 5913, 46233, 409113, 4037913][:len(x)]
plt.plot(x, yTheo, label="Theoretical lengths")
minLengths = comparison(len(x))
for key in minLengths:
	plt.plot(x, minLengths[key], label=key)
plt.legend()
plt.show()