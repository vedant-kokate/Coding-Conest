#!/bin/python3
import sys
import math
from statistics import mean,median,multimode, quantiles, stdev, variance
input=sys.stdin.readline
def I():return list(map(int,input().split()))

n=int(input())
a=I()
a.sort()
# print(quantiles(a,n=4))

# print(a)
if n%2==1:
    print(int(median(a[:len(a)//2])))
    print(int(median(a)))
    print(int(median(a[len(a)//2+1:])))
else:
    print(int(median(a[:len(a)//2])))
    print(int((median(a))))
    print(int(median(a[len(a)//2:])))

