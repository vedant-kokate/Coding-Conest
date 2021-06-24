import sys
from math import gcd
input = sys.stdin.readline

for _  in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(n):
        temp=a[i]
        if temp%2==0:
            ans+=n-i-1
            continue
        for j in range(i+1,n):
            if gcd(2*a[i],a[j])>1:
                ans+=1
    print(ans)
