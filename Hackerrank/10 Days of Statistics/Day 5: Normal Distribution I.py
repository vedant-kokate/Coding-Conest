import math

phi=lambda x: (1+math.erf((x-mean)/(math.sqrt(2)*std)))/2

mean,std=map(int,input().split())
x1=float(input())
ans=phi(x1)
print(round(ans,3))

x2,x3=map(float,input().split())
ans=phi(x3)-phi(x2)
print(round(ans,3))
