import sys
input=sys.stdin.readline
from heapq import heapify,heappop, heappush
from collections import defaultdict,deque
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    n=int(input())
    fun = f()
    fun.insert(0, 0)
    point = f()
    point.insert(0, 0)
    par=defaultdict(list)
    for i,val in enumerate(point):
        if i==0:
            continue
        par[val].append(i+1)
    # print(par)
    ans = 0
    q = deque()
    for key in range(n+1):
        if len(par[key]) ==0:
            q.append(key)
    l = defaultdict(list)
    while q:
        # print(q)
        x = q.popleft()
        # print('x=',x,point[x])
        l[point[x]].append(fun[x])
        if len(l[point[x]]) == len(par[point[x]]):
            q.append(point[x])
            fun[point[x]] = max(fun[point[x]],min(l[point[x]]))
            ans += sum(l[point[x]]) - min(l[point[x]])
        # print(fun,ans) 
        # l[x].append(fun[x])

    # print(fun)
    ans+=fun[0]
    print(f"Case #{_+1}: {ans}")
    