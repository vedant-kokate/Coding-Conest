from math import sqrt
def f(n,y):
    x1 = (n*n*y + sqrt(y*y*n**4 - 4*(y*y-n*n)))/2
    x2 = (n*n*y - sqrt(y*y*n**4 - 4*(y*y-n*n)))/2
    return [x1,x2]

n,y=map(int, input().split())
print(f(n,y))