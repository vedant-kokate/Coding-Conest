import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))
# def brute(n,k,s):
#     a=[]
#     a[:]=s
#     a2=a.copy()
#     for K in range(k):
#         for i,val in enumerate(a):
#             if val=='1':
#                 if i+1<n and a[i+1]=='0':
#                     a2[i+1]='1'
#                 if i-1>=0 and a[i-1]=='0':
#                     a2[i-1]='1'
#                 a2[i]='0'
  
#         a=a2.copy()
#         s2="".join(a2)

#         print(s2,K+1)
#     return(s2)
# mod=10**9+7
for _ in range(int(input())):
    n,k=I()
    s=input().strip()
    # brute(n,k,s)
    a=[]
    a[:]=s
    # print(s)
    dp=[10**10]*n
    last_zero=-1
    for i,val in enumerate(a):
        if val=='1':
            if i-1>=0 and a[i-1]=='0':
                dp[i]=0
            elif i+1<n and a[i+1]=='0':
                dp[i]=0
            elif last_zero!=-1:
                dp[i]=i-last_zero+1
        else:
            last_zero=i
            if i-1>=0:
                dp[i]=dp[i-1]+1

    last_zero=-1
    for i in range(n-1,-1,-1):
        val=a[i]
        if val=='0':
            last_zero=i
            if i+1<n:
                dp[i]=min(dp[i],dp[i+1]+1)
        else:
            if last_zero!=-1:
                dp[i]=min(last_zero-i+1,dp[i])
    # print(dp)
    ans=['0']*n
    for i in range(n):
        if (k+dp[i])%2==0 and dp[i]<=k:
            ans[i]='1'
    print("".join(ans))


