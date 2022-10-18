from heapq import heapify,heappop,heappush
import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n,d=I()
    days=defaultdict(list)
    for i in range(n):
        di, ti, si = I()
        days[di].append((si,ti))
    heap=[]
    for day in range(1,d+1):
        for si,ti in days[day]:
            heappush(heap, (-si,-ti))
        if heap:
            si,ti=heappop(heap)
            if ti!=-1:
                heappush(heap, (si,ti+1))
    ans=0
    for si,ti in heap:
        ans += -si*-ti
    print(ans)
    


