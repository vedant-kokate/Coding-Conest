import sys
input = sys.stdin.readline
from bisect import bisect_left
from heapq import heappop,heappush
from collections import deque
from random import randint
def I():return list(map(int,input().split()))
def f():
    for k in range(1,101):
        q = []
        for i in a:
            q.append(i)
        q.sort()
        for i in range(1,k+1):
            # print(q,k,i)
            val = k-i+1
            p = bisect_left(q, val)
            if not q or q[min(p,n-1)]>val:
                return k-1
            del q[min(p,n-1)]
            if q:
                item = q.pop(0) +val
                q.insert(p,item)


for _  in range(5):
# for _  in range(int(input())):
    n = 5
    if n==1:
        a = int(input())
        if a==1:
            print(1)
        else:
            print(0)
        continue
    heap=[]
    a=[]
    for x in range(n):
        a.append(randint(1,n))
    print(a)
    print(f())
    
            

    