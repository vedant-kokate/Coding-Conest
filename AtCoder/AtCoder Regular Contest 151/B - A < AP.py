import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
from collections import defaultdict

def f(v,vis,stack):
    # print(v,vis,stack)
    vis[v] = True
 
    # Recur for all the vertices adjacent to this vertex
    for i in g[v]:
        if i not in vis:
            f(i, vis, stack)

    # Push current vertex to stack which stores result
    stack.append(v)

# input
n,m=I()
a=I()
same = 0
g = defaultdict(list)

for i,val in enumerate(a):
    if val == i+1:
        same += 1
    elif val >i+1:
        g[val].append(i+1)
    else:
        g[i+1].append(val)
# print(g,same)
vis={}
stack=[]
for i in range(1,n+1):
    if i not in vis:
        f(i,vis,stack)
mod=998244353
print((pow(m,n,mod)-n)%mod)
