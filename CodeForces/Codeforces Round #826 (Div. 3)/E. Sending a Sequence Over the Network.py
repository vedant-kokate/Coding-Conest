import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))
def f(a):
    g=defaultdict(set)
    for i,val in enumerate(a):
        if i-val>=0:
            g[i-val].add(i+1)
        if i+val+1<=n:
            g[i].add(i+val+1)
    vis={}
    vis[0]=True
    stack=[0]
    while stack:
        cur = stack.pop()
        if cur==n:
            return True
        for neigh in g[cur]:
            if neigh not in vis:
                stack.append(neigh)
                vis[neigh]=True
    return False
    stack=[]
    print(g)
for _ in range(int(input())):
    n=int(input())
    a=I()
    if f(a):
        print("YES")
    else:
        print("NO")