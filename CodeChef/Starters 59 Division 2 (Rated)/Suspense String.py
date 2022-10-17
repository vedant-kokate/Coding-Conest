import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

mod=10**9+7
for _ in range(int(input())):
    n= int(input())
    a=input().strip()
    l=[]
    l[:]=a
    i=0
    j=n-1
    t=""
    alice=True
    while l:
        if alice:
            ch=l.pop(0)
            if ch+t<t+ch:
                t=ch+t
            else:
                t=t+ch
        else:
            ch=l.pop()
            if ch+t>t+ch:
                t=ch+t
            else:
                t=t+ch
        alice=not alice
    print(t)
 
