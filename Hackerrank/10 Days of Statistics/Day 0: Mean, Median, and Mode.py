import sys
from statistics import mean,median,multimode
input=sys.stdin.readline
def I():return list(map(int,input().split()))

n=int(input())
a=I()
print(mean(a))
print(median(a))
print(min(multimode(a)))