import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    tot_gcd = a[0]
    for i in a:
        tot_gcd = gcd(tot_gcd,i)
    if tot_gcd==1:
        print(0)
        continue
    # one
    ans=n
    for i in range(n):
        val = gcd(a[i],i+1)
        if val==a[i]:
            continue
        if gcd(tot_gcd,val)==1:
            ans=min(ans,n-i)
    # two
    for i in range(n-1):
        val1 = gcd(a[i],i+1)
        val2=gcd(a[i+1],i+2)
        cost = 2*n - 2*i - 1
        ans=min(ans,cost)
    print(ans)

    
