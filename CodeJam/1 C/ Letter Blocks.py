## topological sort and cyclic code borrowed form gfg
import sys
from itertools import permutations
input=sys.stdin.readline
from heapq import heapify,heappop, heappush
from collections import defaultdict,deque
def f():return list(map(int,input().split()))

class Graph:

	def isCyclicUtil(self, v, visited, recStack):

		# Mark current node as visited and
		# adds to recursion stack
		visited[v] = True
		recStack[v] = True

		# Recur for all neighbours
		# if any neighbour is visited and in
		# recStack then graph is cyclic
		for neighbour in self.graph[v]:
			if visited[neighbour] == False:
				if self.isCyclicUtil(neighbour, visited, recStack) == True:
					return True
			elif recStack[neighbour] == True:
				return True

		# The node needs to be popped from
		# recursion stack before function ends
		recStack[v] = False
		return False

	# Returns true if graph is cyclic else false
	def isCyclic(self):
		visited = [False] * (self.V + 1)
		recStack = [False] * (self.V + 1)
		for node in range(self.V):
			if visited[node] == False:
				if self.isCyclicUtil(node,visited,recStack) == True:
					return True
		return False

	def __init__(self, vertices):
		self.graph = defaultdict(list) # dictionary containing adjacency List
		self.V = vertices # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A recursive function used by topologicalSort
	def topologicalSortUtil(self, v, visited, stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Push current vertex to stack which stores result
		stack.append(v)

	# The function to do Topological Sort. It uses recursive
	# topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack = []

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)


		return stack[::-1] # return list in reverse order







def check1(l):
    staring = set()
    ending = set()
    rest = set()
    
    for w in l:
        if len(w)==1:
            continue
        if not check2(w):
            return False
        for lett in range(len(w)):
            if lett ==0:
                if w[lett] in staring or w[lett] in rest:
                 
                    return False
            elif lett == len(w)-1:
                if w[lett] in ending or w[lett] in rest:
                   
                    return False
            else:
                
                if w[lett] in staring or w[lett] in ending or w[lett] in rest:
                   
                    return False
                rest.add(w[lett])
        staring.add(w[0])
        ending.add(w[-1])    
    return True

def check2(w):
    till_now = set()
    last = ""
    for lett in w:
        if lett in till_now and lett!=last:
        
            return False
        last=lett
        till_now.add(lett)
    return True



    
for _ in range(int(input())):
    n = int(input())
    temp_l = input().strip().split()
    l=[]
    for words in temp_l:
        word = ""
        for lett in words:
            if len(word) and word[-1]==lett:
               
                continue
            word+=str(lett)
        l.append(word)
    l2 = list(set(l))
  
    if not check1(l2):
        print(f"Case #{_+1}: IMPOSSIBLE")
        continue
    g= Graph(len(l2))
    for i in range(len(l2)):
        for j in range(len(l2)):
            if i==j:
                continue 
            if l2[i][-1]==l2[j][0]:
                g.addEdge(i,j)
    if g.isCyclic():
        print(f"Case #{_+1}: IMPOSSIBLE")
        continue
    ans = g.topologicalSort()
    ans2=[]
    for i in ans:
        for j in range(len(l)):
            if l2[i]==l[j]:
                ans2.append(temp_l[j])
    final_ans = "".join(ans2)
    print(f"Case #{_+1}: {final_ans}")
 



# Thanks to Divyanshu Mehta for contributing this code
# 9912991991