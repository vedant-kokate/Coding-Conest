import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush
from math import gcd
def I():return list(map(int,input().split()))
def f(y,x):
    chain={}
    while x>1 and y>1:
        # print(x,y)
        if (x,y) in chain:
            break 
        chain[(x,y)] = True 
        gcd_=gcd(x,y)
        if x==gcd_:

            return True
        x//=gcd_
        y=gcd_ 
    # print(x,y)

for _ in range(int(input())):

    x,y = I()
    if y==1 or f(x,y):
        print("YES")
    else:
        print("NO")
    
