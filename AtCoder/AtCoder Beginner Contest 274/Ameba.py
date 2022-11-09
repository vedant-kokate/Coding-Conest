import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
from collections import defaultdict
n = int(input())
a = I()
g=defaultdict(list)
for i,val in enumerate(a):
    g[val].append(2*(i+1))
    g[val].append(2*(i+1)+1)
# print(g)
stack=[(1,0)]
ans=[0]*(2*n+2)
while stack:
    cur,dep = stack.pop()
    ans[cur]=dep
    for neigh in g[cur]:
        stack.append((neigh,dep+1))
for i in ans[1:]:
    print(i)