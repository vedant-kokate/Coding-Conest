import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
mod=10**9+7
def I():return list(map(int,input().split()))

def f(idx, parity, k, even, odd):
    global mem 
    if (idx,parity,k,even,odd) in mem:
        return mem[(idx,parity,k,even,odd)] 

    if idx==n and k==0:return 1
    if idx==n or k==0 or even<0 or odd < 0: return 0

    ans=0
    if a[idx]!=0:
        if parity==a[idx]%2:
            ans = f(idx + 1, 1 - parity, k - 1, even, odd) + f(idx + 1, parity, k, even, odd)
    else:
        if parity:
            ans = odd*(f(idx + 1, parity, k, even, odd - 1) + f(idx + 1, 1 - parity, k - 1, even, odd - 1))
        else:
            ans = even*(f(idx + 1, parity, k, even - 1, odd) + f(idx + 1, 1 - parity, k - 1, even - 1, odd))
        ans %= mod
    mem[(idx,parity,k,even,odd)] = ans
    return ans
for _ in range(int(input())):
    ans=0
    n,k=I()
    a=I()
 
    odd,even=n//2+n%2,n//2
    # print(odd,even)
    for i in a:
        if i%2:
            odd-=1
        elif i!=0:
            even-=1
    # print(odd,even)
    mem = {}
    ans = f(0,0,k,even,odd) + f(0,1,k,even,odd)
    ans%=mod
    print(ans)



