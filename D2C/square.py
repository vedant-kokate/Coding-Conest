import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))


n=int(input())
a=[]
for i in range(n):
    # temp=list(map(int,input().split()))
    a.append(input().split())

MAX=10**10
u,d,l,r=-MAX,MAX,MAX,-MAX
for x,y in a:
    u=max(u,y)
    d=min(d,y)
    l=min(l,x)
    r=max(r,x)

hor=abs(l-r)
vert=abs(u-d)
print(max(vert,hor))