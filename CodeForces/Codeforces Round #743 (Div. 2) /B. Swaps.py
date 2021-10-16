import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=f()
    b=f()
    x=[]
    y=[]
    for i,val in enumerate(a):
        x.append([val,i])
    for i,val in enumerate(b):
        y.append([val,i])
    x.sort()
    y.sort()
    for i in range(n-2,-1,-1):
        y[i][1]=min(y[i][1],y[i+1][1])
    ans=10**9
    for i in range(n):
        ans=min(ans,x[i][1]+y[i][1])
    print(ans)
