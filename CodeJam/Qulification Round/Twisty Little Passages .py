import sys
input=sys.stdin.readline
import numpy as np
from heapq import heapify,heappop, heappush
from collections import defaultdict,deque
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    n,k=f()
    arr = np.array(list(range(1,n+1)))
    np.random.shuffle(arr)
    d={}
    cur = 0
    r,p=f()
    d[r] = p 
    
    for i in range(min(k,n)):
        while cur<n and arr[cur] in d:
            cur+=1
        if cur==n:cur = 0
        print('T', arr[cur],flush=True)
        r,p=f()
        d[r] = p 
        
    ans = sum(d.values())*n/len(d)/2
    # print(d,sum(d.values()),len(d),n,flush=True)
    ans = round(ans)
    print('E', ans,flush=True)