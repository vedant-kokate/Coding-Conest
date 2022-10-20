# cook your dish here
import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict,deque
def I():return list(map(int,input().split()))
from time import time
st=time()
def bfs():
    max_dep = 0
    stack= [(0,0)]
    vis={}
    ans = 0
    while True:
        if time()-st>1:
            exit()
        while stack:
            if time()-st>1:
                exit()
            x,y=stack.pop()
            # print(x,y,ans)
            max_dep = max(max_dep,x)
            if x==n-1 and y==m-1:
                return ans
            
            for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                X,Y=x+r,y+c
                
                if 0<=X<n and 0<=Y<m and (X,Y) not in vis and mat[X][Y]=='.':
                    stack.append((X,Y))
                    vis[(X,Y)]= True
        
        if max_dep==n-1:
            ans+=1
            return ans
        ans+=1
        for j in range(m):
            stack.append((max_dep+1,j))
for _ in range(int(input())):
    n,m=I()
    mat=[]
    for i in range(n):
        temp=input().strip()
        mat.append(temp)
    stack=deque([(0,0)])
    # mat[]
    
    print(bfs())
    