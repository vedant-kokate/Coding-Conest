import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().strip().split()))

for _ in range(int(input())):
    n,m,k=f()
    a=[]
    for i in range(n):
        s=input().strip()
        l=[]
        l[:0]=s
        a.append(l)
    # for i in a:
    #     print(i)
    k-=1
    up_count=[0]*m
    down_count=[0]*m
    for col in range(m):
        for row in range(k+1):
            if a[row][col]=='X':
                up_count[col]+=1
        for row in range(k,n):
            if a[row][col]=='X':
                down_count[col]+=1
    # print(up_count)
    # print(down_count)
    # print()
    # print(n-k,k)
    up=[[0]*m for i in range(n-k)]
    down=[[0]*m for i in range(k+1)]
    #up
    for col in range(m):
        count=0
        for row in range(k+1,n+1):
            if row==n:
                if count+up_count[col]==k+1:
                    up[row-k-1][col]=1
            else:
                if count+up_count[col]==k+1:
                    up[row-k-1][col]=1
                else:
                    if a[row][col]=='X':
                        up[row-k-1][col]=1
                        count+=1
    #down
    for col in range(m):
        count=0
        for row in range(k-1,-2,-1):
            if row==-1:
                if count+down_count[col]==n-k:
                    down[k-1-row][col]=1
            else:
                if count+down_count[col]==n-k:
                    down[k-1-row][col]=1
                else:
                    if a[row][col]=='X':
                        down[k-1-row][col]=1
                        count+=1
                    # up[col]+=1
    for col in range(m):
       if count+down_count[col]==n-k:
                down[-1][col]=1

    # for i in up:
    #     print(i)
    # print()
    # for i in down:
    #     print(i)
    ans=10**9
    for i in range(len(up)):
        ans=min(ans,sum(up[i])+i+1)
    for i in range(len(down)):
        ans=min(ans,sum(down[i])+i+1)
    
    count=a[k].count('X')
    ans=min(count,ans)
    print(f"Case #{_+1}: {ans}")
    # print(down)
        

