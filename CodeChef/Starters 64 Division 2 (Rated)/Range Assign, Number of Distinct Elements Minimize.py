import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush
def I():return list(map(int,input().split()))
def f():
    first,last = a[0],a[-1]
    for i in range(n-1):
        if a[i]==first and a[i+1]==last:
            return True 
    return False or first==last
for _ in range(int(input())):
    n = int(input())
    a = I()
    if f():
        print("YES")
    else:
        print("NO")
