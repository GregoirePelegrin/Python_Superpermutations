from itertools import permutations as permutFunction
from matplotlib import pyplot as plt

import SuperpermutationLib as sl

def display(superps):
	lengths = []
	population = []
	for s in superps:
		if s.weight not in lengths:
			lengths.append(s.weight)
			population.append(1)
		else:
			population[lengths.index(s.weight)] += 1
	plt.bar(lengths, population, label="Total: {}".format(len(superps)))
	plt.title("Superpermutation order {}".format(ORDER))
	plt.xlabel("Length")
	plt.ylabel("Occurrences number")
	plt.legend()
	plt.show()

def permutations2(iterable, r=None):
    pool = iterable
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

ORDER = int(input("Number of elts (2-3 for now): "))

# Generate the pool of elts from the number of elt
pool = []
for i in range(ORDER):
	pool.append(chr(65+i))
permutations = list(permutFunction(pool))

# Generate the graph from the permutations
graph = []
for perm in permutations:
	temp = ""
	for elt in perm:
		temp += elt
	graph.append(sl.Node(temp))

# Generate the list of all the superpermutations from the graph => to modify with A*
superpermutations = list(permutations2(graph))
superp = sl.Superpermutation()
for s in superpermutations:
	for n in s:
		superp.include(n)

for i in range(len(superpermutations)):
	temp = sl.Superpermutation()
	for n in superpermutations[i]:
		temp.include(n)
	superpermutations[i] = temp

print(len(superpermutations))

# mini = ORDER**ORDER
# miniSuperp = None
# for s in superpermutations:
# 	if s.weight < mini:
# 		mini = s.weight
# 		miniSuperp = s

# display(superpermutations)