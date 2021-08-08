from heapq import heapify,heappop,heappush
from math import ceil
piles=list(map(int,input().split()))
k=int(input())
for i in range(len(piles)):
    piles[i]=-piles[i]
heapify(piles)
while piles and k:
    
    k-=1
    x=-heappop(piles)
    x=(x+1)//2
    heappush(piles,-x)
    # print(piles,x)
print(-sum(piles)) 