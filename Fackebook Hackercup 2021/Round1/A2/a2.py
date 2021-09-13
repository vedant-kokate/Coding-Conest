import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    x=-1
    o=-1
    last_change=""
    dp=[0]*(n)
    ans=0
    for i,val in enumerate(s):
        if val=='O':
            o=i
        if val=='X':
            x=i
        if o!=-1 and x!=-1:
            if last_change=="":
                if val=='X':
                    dp[i]=o+1
                    last_change="X"
                else:
                    dp[i]=x+1
                    last_change="O"
            else:
                if last_change=='O' and (val=='O' or val=="F"):
                    dp[i]=dp[i-1]                   
                if last_change=='X' and (val=='X' or val=="F"):
                    dp[i]=dp[i-1]
                if last_change=='X' and val=='O':
                    last_change="O"
                    dp[i]=dp[x]+x+1
                if last_change=='O' and val=='X':
                    last_change="X"
                    dp[i]=dp[o]+o+1

    # print(dp)
    mod=1000000007
    print(f"Case #{_+1}: {sum(dp)%mod}")

