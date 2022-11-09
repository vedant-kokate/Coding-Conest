import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))
from random import randint
# for _ in range():
def f(n):
    flag=False
    for i in range(int(sqrt(n))+1):
        j = sqrt(n-i*i)
        if ceil(j)==floor(j):
            flag = True 
            return (i,j) 
    if not flag:
        return (-1,-1)
def f2(n):
    for i in [1,2,3,5,7,11,13,17,19,23]:
        j = sqrt(n-i*i)
        if ceil(j)==floor(j):
            flag = True 
            return (i,j)  
    return (-1,-1)
    
for _ in range(10**3):
    # n = int(input())
    n = randint(1, 10**5)
    ans1=f(n)
    ans2=f2(n)
    if ans1!=ans2:
        print(n,ans1,ans2)
        exit()



