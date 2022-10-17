import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n,k= I()
    a=I()
    d={}
    for i in a:
        if i not in d:
            d[i]=True 
    
    ans1=0
    i=1
    k1=k
    max_=max(a)
    while k1:
        max_=max(max_,i)
        if i not in d:
            ans1 += max_-i
            k1-=1
        i+=1
    ans2=0
    if 2*n not in d:
        # ans2 += 2*n-max(a)
        k-=1
        i=1
        while k:
            if i not in d:
                ans2 += 2*n-i
                k-=1
            i+=1
    # print(ans1,ans2)
    print(max(ans1,ans2))