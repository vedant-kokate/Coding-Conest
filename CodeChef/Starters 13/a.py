import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().strip().split()))

for _ in range(int(input())):
    n,p,x,y=f()
    a=f()
    ans=0
    for i in range(p):
        if a[i]==0:
            ans+=x
        else:
            ans+=y
    print(ans)

