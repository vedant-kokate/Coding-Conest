#!/bin/python3
import sys
import math
from statistics import mean,median,multimode, quantiles, stdev, variance
input=sys.stdin.readline
def I():return list(map(int,input().split()))

n=int(input())
temp=I()
fr=I()
a=[]
for i in range(n):
    a+=[temp[i]]*fr[i]
a.sort()
# print(quantiles(a,n=4))

# print(a)
if n%2==1:
    q1=median(a[:len(a)//2])
    q3=median(a[len(a)//2+1:])

    print("{:.1f}".format(round(q3-q1,1)))
else:
    q1=median(a[:len(a)//2])

    q3=median(a[len(a)//2:])
    print("{:.1f}".format(round(q3-q1,1)))

