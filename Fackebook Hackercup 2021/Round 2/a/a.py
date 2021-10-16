import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().strip().split()))

for _ in range(int(input())):
    n,m=f()
    if n==1:
        s=[int(input())]
        for i in range(n+1):
            x=int(input)
    else:
        d=defaultdict(int)

        temp=f()
        for i,val in enumerate(temp):
            d[val]+=1
        s=temp.copy()
        change=[False]
        ans=0
        for i in range(n):           
            temp=f()
            for j in temp:
                d[j]-=1
            
            for j in d.values():
                if j<0:
                    ans+=(j*-1)
            # print(d,ans,i)
            d=defaultdict(int)
            for j in temp:
                d[j]+=1   

    print(f"Case #{_+1}: {max(0,ans-m)}")

