import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush
from math import gcd
def I():return list(map(int,input().split()))
def f():
    pass
for _ in range(int(input())):
    n = int(input())
    a = I()
    gcd_ = a[0]
    for i in a:
        gcd_ = gcd(i,gcd_)
        if gcd_==1:
            break
    ans = n
    for i in a:
        if i==gcd_:
            ans-=1 
    print(ans) 
