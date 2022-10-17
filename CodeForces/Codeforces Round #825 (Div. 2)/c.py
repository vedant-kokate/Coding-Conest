import sys
input=sys.stdin.readline
from collections import defaultdict
from random import randint
K=26
from bisect import bisect_right as br
def brute(a,n):
    ans = 0
    for i in range(n):
        last=a[i]
        for j in range(n):
            if i+j>=len(a):
                break 
            # print(i,j)
            val = a[i+ j]
            if val>=j+1:
                # print(i,j)
                ans+=1
            else:
                # print(i,j,'b')
                break
    return ans
            

for _ in range(int(input())):
    n=int(input())
    # n = 5
    n+=1
    st=[[0 for i in range(K+1)]for j in range(n+1)]
    a=[]
    # for i in range(5):
        # a.append(randint(1,10))
    a=list(map(int,input().split()))
    # print(a)
    ans2 = brute(a, n-1)
    a.insert(0,0)
    
    
    log=[0]*(n+1)
    for i in range(2,n+1):
        log[i]=log[i//2]+1
    
    d=defaultdict(list)
    for i in range(n):
        st[i][0]=a[i]
        if i>0:
            d[a[i]].append(i)
    
    for j in range(1,K+1):
        i=0
        while i + (1 << j) <= n:
            st[i][j] = min(st[i][j-1], st[i + (1 << (j - 1))][j - 1])
            i+=1
    # print(d)
    dp=[0]*(n+1)
    ans=0
    for i in range(1,n):
        # L,R=map(int,input().split())
        L,R=i+1-a[i],i
        
        if L<1:
            L=1
        # print(L,R)
        j=log[R-L+1]
        minimum = min(st[L][j], st[R - (1 << j) + 1][j])
        pos=br(d[minimum],R)
        # print('pos',pos)
        last = d[minimum][pos-1]
        if last==i:
            dp[i] = min(a[i],i)
        else:
            print(R,last)
            dp[i]=min(dp[last] + R - last,a[i])
    print(dp)    
    # if sum(dp)!=ans2:
    #     print(a)
    #     break
    print(sum(dp),ans2)
	