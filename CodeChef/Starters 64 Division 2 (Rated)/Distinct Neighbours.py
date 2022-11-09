import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush,heapify
from math import gcd
def I():return list(map(int,input().split()))
def f(vals):
    b=[]
    if len(vals)==1 :
      
        if vals[0]>-4:
            return True 
        return False
    heap = vals  
    heapify(vals)
 
    while heap:
  
        first = -heappop(heap)

        if not heap :
            if first//2<=(len(b)+1):
                return True
            else:
                return False
    
        second = -heappop(heap)
     
        first -=1
        second -=1
        if first!=0:
            heappush(heap, -first)
        if second!=0:
            heappush(heap, -second)
        if not b:
            b.append(1)
        else:
            if b[-1]==1:
                b.append(-1)
            else:
                b.append(1)
    # print(b)
    return True

for _ in range(int(input())):

    n = int(input())
    a=I()
 
    d=defaultdict(int)
    for i in a:
        d[i]-=1
   
    if f(list(d.values())):
        print("YES")
    else:
        print("NO")

