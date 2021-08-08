import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
from heapq import heapify,heappop,heappush

milestones=f()

for xxx in range(1):
    for xxxx in range(1):
        a=[]
        ans=0
        heapify(a)
        for i in milestones:
            heappush(a,-i)
        while len(a)>1:
            print(a,ans)
            x=heappop(a)
            y=heappop(a)
            print('x y',x,y)
            if y!=-1:
                y+=1
                x-=y
                ans+=-2*(y)
                y=-1
                print('before pushin',x,y)
                heappush(a,x)
                heappush(a,y)
            else:
                x+=1
                ans+=2
                if x!=0:
                    heappush(a,x)
        if len(a)==1:
            ans+=1
        print(a)
        print(ans) 