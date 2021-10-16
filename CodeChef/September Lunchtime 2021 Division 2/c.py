import sys
import math
input=sys.stdin.readline
def f():return list(map(int,input().split()))
lim=100
dp=[0]*(lim)
dp[1]=1
for i in range(2,lim):
    Min=1
    if i%2==0:
        for j in range(1,20):
            if 2**j>i:
                break
            if i%(2**j)==0:
                Min=min(dp[i//(2**j)],Min)
            else:
                break
        if Min==0:
            dp[i]=1
    else:
        dp[i]=not(dp[i-1])
for i in range(1,lim):
    if dp[i]:
        dp[i]=1
    else:
        dp[i]=0
# print(*dp[:500])
for _ in range(int(input())):
    n=int(input())
    if n<100:
        if dp[n]==1:
            print("Alice")
        else:
            print("bob")
    else:
        x=math.ceil(math.log(n,2))
        if n==2**x or n==2**x-1:
            print("Alice")
        elif n==2**x-2:
            print("Bob")
        elif n%2:
            print("Bob")
        else:
            print("Alice")
    


    