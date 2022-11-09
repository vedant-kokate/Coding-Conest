import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))
from random import randint
# for _ in range():
for _ in range(int(input())):
    n = int(input())
    # n = randint(1, 10**5)
    print(n)
    flag=False
    for i in range(int(sqrt(n))+1):
        j = sqrt(n-i*i)
        if ceil(j)==floor(j):
            flag = True 
            print(i,j)
            break 
    if not flag:
        print(-1)



