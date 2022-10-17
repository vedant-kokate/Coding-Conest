import sys
input = sys.stdin.readline
from math import sqrt
from collections import defaultdict,deque
def I():return list(map(int,input().split()))
def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)==m
n,m=I()
a=[[-1]*n for i in range(n)]
a[0][0]=0

sq={}
sq[0]=True
for i in range(1,10**3+1):
    sq[i*i]=True

var=set()
for i in sq:
    if m-i in sq:
        var.add((int(sqrt(min(i,m-i))),int(sqrt(max(i,m-i)))))
        # var.add((int(sqrt(max(i,m-i))),int(sqrt(min(i,m-i)))))
if len(var)==0:
    for i in a:
        print(*i)
    exit()
# print(var)
stack=deque([(0,0,0)])
vis={}
vis[(0,0)]=True
while stack:
    
    x,y,d=stack.popleft()
    # print("x","y",x,y,d)
    for r,c in var:
        pos=[(x+r,y+c),(x-r,y+c),
        (x+r,y-c),(x-r,y-c),(x+c,y+r),
        (x-c,y+r),(x+c,y-r),(x-c,y-r),]
        for x1,y1 in pos:
            # print(x1,y1)
            if 0<=x1<n and 0<=y1<n and (x1,y1)not in vis:
                stack.append((x1,y1,d+1))
                # print("a",x1,y1)
                a[x1][y1]=d+1
                vis[(x1,y1)]=True

for i in a:
    print(*i)

    
        