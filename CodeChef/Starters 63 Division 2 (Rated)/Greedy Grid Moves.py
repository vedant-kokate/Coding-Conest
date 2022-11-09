import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush
def I():return list(map(int,input().split()))
def f():
    heap =[(mat[0][0],0,0)]
    while heap:
        val,i,j=heappop(heap)
        if i==n-1 and j==m-1:
            return val 
        if i==n-1:
            heappush(heap, (max(val,mat[i][j+1]),i,j+1))
        elif j==m-1:
            heappush(heap, (max(val,mat[i+1][j]),i+1,j))
        elif (i+j)%2:
            if mat[i+1][j]>mat[i][j+1]:
                heappush(heap, (max(val,mat[i+1][j]),i+1,j))
            else:
                heappush(heap, (max(val,mat[i][j+1]),i,j+1))
        else:
            heappush(heap, (max(val,mat[i][j+1]),i,j+1))
            heappush(heap, (max(val,mat[i+1][j]),i+1,j))
for _ in range(int(input())):
    n,m=I()
    mat=[]
    for i in range(n):
        mat.append(I())
    edges = [[10**6]*m for i in range(n)]
    edges[0][0]=mat[0][0]
    for i in range(n):
        for j in range(m):
            if edges[i][j]!=10**6:
                if (i+j)%2:
                    if i==n-1 and j==m-1:
                        continue
                    elif i==n-1:
                        edges[i][j+1] = min(edges[i][j+1],max(edges[i][j],mat[i][j+1]))
                    elif j==m-1:
                        edges[i+1][j] = min(edges[i+1][j],max(edges[i][j],mat[i+1][j]))
                    elif mat[i+1][j]>mat[i][j+1]:
                        edges[i+1][j] = min(edges[i+1][j],max(edges[i][j],mat[i+1][j]))
                    else:
                        edges[i][j+1] = min(edges[i][j+1],max(edges[i][j],mat[i][j+1]))
                else:
                    if i+1<n:
                        edges[i+1][j] = min(edges[i+1][j],max(edges[i][j],mat[i+1][j]))
                    if j+1<m:
                        edges[i][j+1] = min(edges[i][j+1],max(edges[i][j],mat[i][j+1]))
    # for i in edges:
    #     print(i)
    print(edges[-1][-1])

