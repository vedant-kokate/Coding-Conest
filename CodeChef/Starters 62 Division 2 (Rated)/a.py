import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n,q=I()
    a=I()
    ans=sum(a)
    for i in range(q):
        l,r=I()
        if (r-l)%2==0:
            ans+=1
    print(ans)



