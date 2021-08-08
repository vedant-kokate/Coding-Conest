#!/bin/python3
import sys
import math
from statistics import mean,median,multimode, stdev, variance
input=sys.stdin.readline
def I():return list(map(int,input().split()))

n=int(input())
a=I()
m=mean(a)
var=(sum((m-i)**2 for i in a) )/n
print(round(math.sqrt(var)),1)
