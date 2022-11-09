import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))
from random import randint
for _ in range(int(input())):
    n = int(input())
    # n = randint(1, 10**5)
    s=input()
    one,zero=-1,-1
    for i in range(n):
        if s[i]=='0':
            zero=i
            break
    for i in range(n):
        if s[i]=='1':
            one=i
            break
    if one==-1 or zero==-1:
        print(0)
        continue
    l=min(n-zero,n-one)
    print(one,zero,l)


