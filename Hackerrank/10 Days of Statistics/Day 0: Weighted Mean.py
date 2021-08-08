import sys
from statistics import mean,median,multimode
input=sys.stdin.readline
def I():return list(map(int,input().split()))

n=int(input())
a=I()
w=I()
# print(mean(a))
for i in range(n):
    a[i]=a[i]*w[i]
print(round(sum(a)/sum(w),1))