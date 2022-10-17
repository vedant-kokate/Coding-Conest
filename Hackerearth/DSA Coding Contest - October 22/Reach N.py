import sys
from math import log2
input=sys.stdin.readline
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=f()
    dp=[-10**10]*n 
    dp[0]=a[0]

    # lim=int(log2(n))+1
    for i in range(1,n):
        for j in range(n):
            val=i-(1<<j)
            # print(i,j,val)
            if val <0:
                break 
            v2=a[i]+dp[val]
            if v2>dp[i]:
                dp[i]=v2
            # dp[i]=max(dp[i],)
    print(dp[-1])

