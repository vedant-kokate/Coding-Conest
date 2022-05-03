import sys
input=sys.stdin.readline
from heapq import heapify,heappop, heappush
from collections import defaultdict,deque
def f():return list(map(int,input().split()))

def d(s,i):
    return s[:i]+s[i]+s[i:]

for _ in range(int(input())):
    s = input().strip()
    n=len(s)
    i = 0
    while i<len(s):
        s2 = d(s,i)
        if s2<s:
            s=s2
            i+=1
        i+=1
    print(f"Case #{_+1}: {s}")
    
    
