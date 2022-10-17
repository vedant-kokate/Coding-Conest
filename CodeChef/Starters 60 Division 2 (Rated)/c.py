import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))
def f(a1,a2):
    score=0
    for i in range(len(a1)-1,-1,-1):
        if a1[i]+score > a2[i]:
            return -1
        else:
            score += a2[i]-a1[i]-score
    return score
for _ in range(int(input())):
    n = int(input())
    a=I()
    if a==a[::-1]:
        print(0)
        continue
    if n%2:
        a1=a[:n//2]
        a2=a[n//2+1:]
        a2=a2[::-1]
    else:
        a1=a[:n//2]
        a2=a[n//2:]
        a2=a2[::-1]
    print(f(a1,a2))


    