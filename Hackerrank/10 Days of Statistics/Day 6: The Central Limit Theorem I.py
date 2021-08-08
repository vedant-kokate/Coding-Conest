from math import erf,sqrt
max_weight = float(input())
n = int(input())
mu = float(input())
std_ = float(input())
mean = n*mu
std = (sqrt(n))*std_
phi=lambda x: (1+erf((x-mean)/(sqrt(2)*std)))/2
pro = phi(max_weight)
pro = round(pro, 4)
print(pro)
# import math

# x = int(input())
# n = int(input())
# mu = int(input())
# sigma = int(input())

# mu_sum = n * mu 
# sigma_sum = math.sqrt(n) * sigma

# def cdf(x, mu, sigma):
#     Z = (x - mu)/sigma
#     return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

# print(round(cdf(x, mu_sum, sigma_sum), 4))