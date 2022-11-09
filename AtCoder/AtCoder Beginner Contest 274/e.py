import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
from math import sqrt
ans=10**10
def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
def f(x,y,vis,till_now,acc):
    global ans
    if till_now + dist(x,y,0,0)/(2**m)>ans:
        return
    # print(x,y,vis,till_now,acc)
    p=[]
    for i,j in a:
        if (i,j) not in vis:
            p.append((dist(x,y,i,j)/acc,i,j))
    # print(p)
    if p==[]:
        till_now+=dist(x,y,0,0)/acc
        ans=min(till_now,ans)
        return

    p.sort()
    for d,i,j in p:
        f(i,j,vis|{(i,j)},till_now+d,acc)
    c=[]
    for i,j in b:
        if (i,j) not in vis:
            c.append((dist(x,y,i,j)/acc,i,j))
    c.sort()
    for d,i,j in c:
        f(i,j,vis|{(i,j)},till_now+d,acc*2)


n, m = I()
a = []
for i in range(n):
    x,y=I()
    a.append((x,y))
b=[]
for j in range(m):
    x,y=I()
    b.append((x,y))

f(0,0,set(),0,1)
print(ans)


