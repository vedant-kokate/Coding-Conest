import sys
input=sys.stdin.readline
from math import sqrt
# from random import randint
from collections import defaultdict
from heapq import heappop,heappush
def I():return list(map(int,input().split()))

for _ in range(int(input())):
# for _ in range(10):
    n = int(input())
    red=I()
    blue=I()
    dp=[-1]*(sum(red)+1)
    dp[sum(red)]=0
    for i in range(n):
        # print(dp)
        for j in range(len(dp)):
            if j+red[i]>=len(dp):
                break 
            if dp[j+red[i]]!=-1:
                dp[j]=max(dp[j],dp[j+red[i]] + blue[i])
    ans=0
    for i in range(len(dp)):
        ans=max(ans, min(i,dp[i]))
    print(ans)