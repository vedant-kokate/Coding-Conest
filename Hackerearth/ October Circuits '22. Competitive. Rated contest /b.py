import sys
from collections import defaultdict
input=sys.stdin.readline
def I():return list(map(int,input().split()))
def dfs(g,node):
    stack=[node]
    vis = {}
    vis[node]=True
    while stack:
        cur = stack.pop()
        for neigh in g[cur]:



for _ in range(int(input())):
    n = int(input())
    comp_g = defaultdict(list)
    other_g = defaultdict(list)
    path_sum = defaultdict(int)
    for i in range(n-1):
        a,b,t,val=I()
        comp_g[a].append(b)
        comp_g[a].append(a)
        path_sum[(min(a,b),max(a,b))] = val 

        if t==1:
            other_g[a].append(b)
            other_g[a].append(a)
    




# print(dp[-1])

