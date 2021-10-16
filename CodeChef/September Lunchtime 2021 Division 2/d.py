from bisect import bisect_left
import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
 
def LIS(a):
    n=len(a)
    d=[1]*n
    p=[-1]*n
    for i in range(n):
        for j in range(i):
            if a[j]<=a[i] and d[i]<d[j]+1:
                d[i]=d[j]+1
                p[i]=j
    ans=d[0]
    pos=0
    for i in range(n):
        if d[i]>ans:
            ans=d[i]
            pos=i
    subseq=[]
    while pos!=-1:
        subseq.append(a[pos])
        pos=p[pos]
    return subseq[::-1]
def lcs(X , Y):
    
    m = len(X)
    n = len(Y)
 
    
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]
 
for _ in range(int(input())):
    n=int(input())
    v=f()
    lnd=LIS(v)
    lni=LIS(v[::-1])
    # print(lnd)
    # print(lni[::-1])
    print(lcs(lnd,lni))