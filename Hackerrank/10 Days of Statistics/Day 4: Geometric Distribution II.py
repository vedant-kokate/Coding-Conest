import math 

def g(n,p):
    return pow(1-p,n-1)*p

l,r=map(int,input().split())
p=l/r
n=int(input())

ans=sum(g(i,p) for i in range(1,6))

print(round(ans,3))