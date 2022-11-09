import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict,deque
from heapq import heappop,heappush
from math import gcd
from time import time
def I():return list(map(int,input().split()))
prime_list=[]
lim=10**6
prime=[True]*(1+lim)
for i in range(2,lim):
    if prime[i]:
        prime_list.append(i)
        for j in range(i*i,lim,i):
            prime[j]=False 

print("start")
def brute(x,y):
    
    i=0
    fact=[]
    # print(x,y)
    while y>1 and i<len(prime_list):
        # print(y,i)
        val = prime_list[i]
        if y%val==0:
            fact.append(val)
            while y%val==0:
                y//=val 
        i+=1
    for i in fact:
        if x%i!=0:
            return False 
    return True
def f(y,x):
    chain={}
    while x>1 and y>1:
        # print(x,y)
        # if (x,y) in chain:
        #     break 
        # chain[(x,y)] = True 
        gcd_=gcd(x,y)
        if x==gcd_:

            return True
        x//=gcd_
        y=gcd_ 
    return False
    # print(x,y)

for _ in range(int(input())):

    x,y = I()
    a1=y==1 or f(x,y)
    a2=brute(x, y)
    if a1!=a2:
        print(x,y,a1,a2)
print("done")
    


