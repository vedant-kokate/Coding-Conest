import math 

def b(n,x,p):
    return math.comb(n,x)*pow(p,x)*pow(1-p,n-x)
x,y=map(float,input().split())
odd=x/y
p=x/(x+y)
ans=0
for i in range(3,7):
    ans+=b(6,i,p)
print(round(ans,3))
# print(p,math.comb(6,3))
# print(round(1-20*(p**3)*((1-p)**3),3))