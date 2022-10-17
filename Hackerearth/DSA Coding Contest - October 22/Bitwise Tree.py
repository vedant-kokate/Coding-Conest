import sys
from collections import defaultdict
input=sys.stdin.readline
def f():return list(map(int,input().split()))

n=int(input())
a=f()
a.insert(0, 0)
g=defaultdict(list)


# lim=int(log2(n))+1
for i in range(1,n):
    x,y=f()
    g[x].append(y)
    g[y].append(x)
vis={}
# print(g)
ans1=0
for i in range(1,n+1):
    # print(i,g[i])
    if i in vis:
        continue

    tot=a[g[i][0]]
    vis[g[i][0]]=True

    for x in range(1,len(g[i])):
        tot|=a[g[i][x]]
        vis[g[i][x]]=True

    while tot&a[i]!=0:
        a[i]>>=1
        ans1 += 1
print(ans1)

ans2=0
stack=[g[1][0]]

while stack:
    i=stack.pop()
    tot=0
    for n in g[i]:
        tot |= n
        if n not in vis:
            stack.append(n)
        if i in vis:
            vis[n]=True
    
    
    # print(i,g[i])
    if i in vis:
        continue

    # tot=a[g[i][0]]
    # vis[g[i][0]]=True

    # for x in range(1,len(g[i])):
    #     tot|=a[g[i][x]]
    #     vis[g[i][x]]=True

    while tot&a[i]!=0:
        a[i]>>=1
        ans2 += 1
print(ans2)
    
    




# print(dp[-1])

