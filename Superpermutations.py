from itertools import permutations as permutFunction

import SuperpermutationLib as sl

ORDER = int(input("Number of elts: "))
# Generate the pool of elts from the number of elt
pool = []
for i in range(ORDER):
	pool.append(chr(65+i))
permutations = list(permutFunction(pool))

graph = []
for perm in permutations:
	graph.append(sl.Node(perm))