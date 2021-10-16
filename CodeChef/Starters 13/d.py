import sys
input=sys.stdin.readline
from math import gcd,sqrt,log,ceil,floor
from collections import defaultdict
def f():return list(map(int,input().strip().split()))


def solve(a,b):
    if a==1:
        return("YES")
    x=gcd(a,b)    
    if x==1:
        return "NO"
    if floor(log(a,x))==ceil(log(a,x)):
        return "YES"
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            while a%i==0:
                a//=i
            while b%i==0:
                b//=i
            return solve(a,b)
    while a%x==0:
        a//=x
    while b%x==0:
        b//=x
    if a==1:
        return "YES"
    return "NO"

for _ in range(int(input())):
    a,b=f()
    print(solve(a,b))
