import sys
input=sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    vis=[False]*n
    stack=deque()
    for i in range(n):
        if a[i]>0:
            stack.append((i,k))
            vis[i]=True
    
    while stack:
        # print(stack)
        pos,val=stack.popleft()
        index1= (pos-1)%n
        index2= (pos+1)%n 
        a[index1]+=val
        a[index2]+=val
        if val>0:
            if vis[index1]==False:
                stack.append((index1,val-1))
            if vis[index2]==False:
                stack.append((index2,val-1))
        vis[index1]=True
        vis[index2]=True
    print(sum(a))

        

