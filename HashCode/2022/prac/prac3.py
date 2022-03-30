def is_clique(b):

	for i in range(1, b):
		for j in range(i + 1, b):
			if (graph[store[i]][store[j]] == 0):
				return False	
	return True

def maxCliques(i, l):
	print('l',l)
	max_ = 0
	for j in range(i + 1, n + 1):
		store[l] = j

		if (is_clique(l + 1)):
			max_ = max(max_, l)
			max_ = max(max_, maxCliques(j, l + 1))
		
	return max_

MAX = 100
store = [0] * MAX
graph = [[0 for i in range(MAX)] for j in range(MAX)]
d = [0] * MAX
edges = [[ 1, 2 ],[ 1, 3 ],[ 1, 4 ],[1,5],
[ 2, 3 ],[ 2, 4 ],[2,5],
	[ 3, 4 ],[3,5],
	[4,5]
		]
size = len(edges)
n = 5
for i in range(size):
	graph[edges[i][0]][edges[i][1]] = 1
	graph[edges[i][1]][edges[i][0]] = 1
	d[edges[i][0]] += 1
	d[edges[i][1]] += 1
	
print(maxCliques(0, 1))
print(store)
# This code is contributed by PrinciRaj1992
