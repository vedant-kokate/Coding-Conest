import sys
input=sys.stdin.readline
from heapq import heapify, heappop,heappush
def I():return list(map(int,input().split()))
for _ in range(int(input())):
    n,k,s=I()
    arr=I()
    a=[0]*n
    a[0]=arr[0]
    for i in range(1,n):
        a[i]=a[i-1]+arr[i]

    a.insert(0,0)
    # print(a)
   
    d={}
    for i in range(1,n+1):
        l=i+1
        u=n
        
        while l<u:
            mid=(l+u)//2
            val=a[mid]-a[i-1]
            # print(val,mid)
            if val==s:
                l=mid
                break
            elif val>s:
                u=mid
            else:
                l=mid+1
            
        val=a[u]-a[i-1]
        if val>s:
            u-=1

        # print(a[u]-a[i-1],u,'check',i)  
        d[i]=u  
    # print(d)
    heap=[]
    heapify(heap)
    i=1
    last=-1
    while i<n+1 and len(heap)<k:
        last=d[i]
        heappush(heap,i)
        
        i=d[i]+1
        
    # print(len(heap))
    # print(heap)
    # print(last,'last')
    ans=1
    while i<n+1:
        low=heappop(heap)
        # print(low,i,'low up')
        ans=max(ans,last-low+1)
        heappush(heap,i)
        last=d[i]
        i=d[i]+1
    low=heappop(heap)
    ans=max(ans,last-low)
    print(ans)