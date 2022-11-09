import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush
from math import gcd
def I():return list(map(int,input().split()))

for _ in range(int(input())):

    n =int(input())
    a=I()
    a1 = [a[0]]
    ans = 0
    for i in range(1,n):
        val=a[i]
        if val==1:
            a1.append(val)
            continue
        while val<a1[-1]:
            val=val*val 
            ans+=1
        a1.append(val)
    print(a1,ans)