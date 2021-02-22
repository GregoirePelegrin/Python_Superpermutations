from itertools import permutations

# TODO: Generate every permutation
n = int(input("Number of elts: "))
# Generate the pool of elts from the number of elt
pool = []
for i in range(n):
	pool.append(chr(65+i))
perm = list(permutations(pool))
print(perm)

# TODO: Make the graph
# TODO: A* algorithm in the graph