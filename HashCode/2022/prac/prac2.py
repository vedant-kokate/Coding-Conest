from collections import defaultdict
from fractions import Fraction as frac
from sys import stdin
input = stdin.readline

def score_count(ing_list):
    score=0
    for i in range(c):
        flag=True
        for l in p[i]['like']:
            if l not in ing_list:
                flag=False
                break
        for l in p[i]['dislike']:
            if l in ing_list:
                flag=False
                break
        if flag:
            score+=1
    return score


f_input = open('b_basic.in.txt','r')
c=int(f_input.readline())
p=defaultdict(dict)
ing=defaultdict(dict)
for i in range(c):
    n,*l=f_input.readline().split()
    n=int(n)
    p[i]['like'] = set(l)
    for indi_ing in l:
        if 'like' in ing[indi_ing]:
            ing[indi_ing]['like'].add(i)
        else:
            ing[indi_ing]['like'] = set()
            ing[indi_ing]['like'].add(i)

    n2,*l=f_input.readline().split()
    n2=int(n2)
    p[i]['dislike'] = set(l)

    for indi_ing in l:
        if 'dislike' in ing[indi_ing]:
            ing[indi_ing]['dislike'].add(i)
        else:
            ing[indi_ing]['dislike'] = set()
            ing[indi_ing]['dislike'].add(i)

    p[i]['val'] = frac(1,(n+n2))




def is_clique(b):

	for i in range(1, b):
		for j in range(i + 1, b):
			if (graph[store[i]][store[j]] == 0):
				return False	
	return True

def maxCliques(i, l):
	max_ = 0
	for j in range(i + 1, n + 1):
		store[l] = j

		if (is_clique(l + 1)):
			max_ = max(max_, l)
			max_ = max(max_, maxCliques(j, l + 1))
		
	return max_

MAX = 100
store = [0] * (MAX+1)
d = [0] * MAX
n = c

graph=[[0 for i in range(MAX)] for j in range(MAX)]
d = [0] * MAX
for i in range(c):
    for j in range(i+1,c):
        if p[i]['like']-p[j]['dislike']==p[i]['like'] and p[j]['like']-p[i]['dislike']==p[j]['like']:
            graph[i+1][j+1]=1
            graph[j+1][i+1]=1
            d[i+1]+=1
            d[j+1]+=1

# print(graph)
# print(d)
print(maxCliques(0, 1))
print(store[:6])

# This code is contributed by PrinciRaj1992
