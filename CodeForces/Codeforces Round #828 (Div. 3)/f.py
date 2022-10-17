import sys
input=sys.stdin.readline
from collections import defaultdict
from math import log2
def I():return list(map(int,input().split()))
from math import gcd,sqrt

def f(a,b,c,d):
    n=a
    fact={}
    for i in range(2,int(sqrt(a))+2):
        while n%i==0:
            n//=i
            if i in fact:
                fact[i]+=1
            else:
                fact[i]=1
    if n>1:
        fact[n]=1
    print(fact)
    # val=a*b
    # for i in range(a+1,c+1):
    #     n2=val//gcd(val, i)
    #     # print(n2,"n2",i,val)
    #     if n2<=d:
    #         n3=(d//n2)*n2
    #         # print(n3,b,d)
    #         if b<n3<=d:
    #             return i,n3
    # return -1,-1
for _ in range(int(input())):
    a,b,c,d=I()
    print(*f(a,b,c,d))
    
            
