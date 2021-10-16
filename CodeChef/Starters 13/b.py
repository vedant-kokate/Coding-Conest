import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().strip().split()))

for _ in range(int(input())):
    p,a,b,c,x,y=f()
    cost=min(x*a+b,y*a+c)
    ans=p//cost
    print(ans)

