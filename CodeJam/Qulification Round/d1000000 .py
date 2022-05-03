import sys
input=sys.stdin.readline
from heapq import heapify,heappop, heappush
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    n=int(input())
    a = f()
    heapify(a)
    cur = 1
    while a:
        x=heappop(a)
        if x>=cur:
            cur+=1
    print(f"Case #{_+1}: {cur-1}")
    
    # print(*ans)