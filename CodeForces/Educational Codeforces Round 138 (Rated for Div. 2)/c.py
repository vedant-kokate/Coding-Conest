import sys
input = sys.stdin.readline
from bisect import bisect_left
from heapq import heappop,heappush
from collections import deque
def I():return list(map(int,input().split()))
def f():
    a.sort()
    for k in range(1,101):
        
        x=2*k-1
        # print(k,"k",x)
        if x>n:
            return k-1
        ele=1
        for i in range(k-1,x):
            # print(i,a[i])
            if a[i]>ele:
                return k-1
            ele+=1
            

for _  in range(int(input())):
    n = int(input())
    if n==1:
        a = int(input())
        if a==1:
            print(1)
        else:
            print(0)
        continue
    
    a = I()
    print(f())
    
            

    