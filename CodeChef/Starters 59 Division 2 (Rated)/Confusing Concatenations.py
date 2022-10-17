import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

mod=10**9+7
for _ in range(int(input())):
    n=int(input())
    l=I()
    a=[]
    b=[]
    flag=False
    for i in range(1,n):
        if l[i]>l[0]:
            pos=i 
            flag=True
            break
    
    if flag:
        a=l[:i]
        b=l[i:]
        print(len(a))
        print(*a)
        print(len(b))
        print(*b)
    else:
        print(-1)


