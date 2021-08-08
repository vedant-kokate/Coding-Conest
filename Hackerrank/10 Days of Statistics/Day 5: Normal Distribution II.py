import math

phi=lambda x: (1+math.erf((x-mean)/(math.sqrt(2)*std)))/2

mean,std=map(int,input().split())
x1=float(input())
ans=(1-phi(x1))*100
print(round(ans,2))

x2=float(input())
ans=(1-phi(x2))*100
print(round(ans,2))

ans=(phi(x2))*100
print(round(ans,2))
# import math
# mean, std = 70, 10
# cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


# print(round((1-cdf(80))*100,2))
# print(round((1-cdf(60))*100,2))
# print(round((cdf(60))*100,2))