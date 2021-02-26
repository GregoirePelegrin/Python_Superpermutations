from itertools import permutations as permutFunction

import SuperpermutationLib as sl

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

ORDER = int(input("Number of elts: "))
# Generate the pool of elts from the number of elt
pool = []
for i in range(ORDER):
	pool.append(chr(65+i))
permutations = list(permutFunction(pool))

graph = []
for perm in permutations:
	temp = ""
	for elt in perm:
		temp += elt
	graph.append(sl.Node(temp))

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
print("List:")
for s in superpermutations:
	print(s.__str__())