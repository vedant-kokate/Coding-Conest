import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

def factors(n,k):
    d=defaultdict(int)
    i=2
    while n>1:
        if n%i==0:
            d[i]+=1
            n//=i
        else:
            i+=1

    upper = pow(2,k,mod)
    ans=1
    for key,val in d.items():
        val2 = (val*upper-val)%mod
        ans *= (pow(key,val2+1,mod)-1)%mod*pow(key-1,mod-2,mod)
        ans %= mod
    return d,ans

mod=10**9+7
for _ in range(int(input())):
    n,k=I()
    d,ans=factors(n,k)
    ans *= n
    print(ans%mod)
 
