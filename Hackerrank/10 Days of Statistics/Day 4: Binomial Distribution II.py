import math 

def b(n,x,p):
    return math.comb(n,x)*pow(p,x)*pow(1-p,n-x)
p,n=map(int,input().split())
p/=100

ans=sum(b(n,i,p) for i in range(3))
print(round(ans,3))

ans=sum(b(n,i,p) for i in range(2,11))
print(round(ans,3))