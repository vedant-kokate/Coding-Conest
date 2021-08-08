from math import erf,sqrt
sample=int(input())
mu=int(input())
sigma=int(input())
per=float(input())
z=float(input())

sigmaS=sigma/(sqrt(sample))

A=mu - (z*sigmaS)
B=mu + (z*sigmaS)

print(round(A,2))
print(round(B,2))