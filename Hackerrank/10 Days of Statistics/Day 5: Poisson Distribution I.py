import math 

def P(k,avg):
    return pow(avg,k)*pow(math.e,-avg)/math.factorial(k)

avg=float(input())
k=int(input())

ans=P(k,avg)

print(round(ans,3))