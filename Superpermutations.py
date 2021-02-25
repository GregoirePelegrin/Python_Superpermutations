from itertools import permutations as permutFunction

import NodeLib as nl

# TODO: Generate every permutation
ORDER = int(input("Number of elts: "))
# Generate the pool of elts from the number of elt
pool = []
for i in range(ORDER):
	pool.append(chr(65+i))
permutations = list(permutFunction(pool))

# TODO: Make the graph
graph = []
for perm in permutations:
	graph.append(nl.Node(perm))
print("{} -> {} = {}".format(graph[0], graph[1], graph[0].distance(graph[1])))
# TODO: A* algorithm in the graph