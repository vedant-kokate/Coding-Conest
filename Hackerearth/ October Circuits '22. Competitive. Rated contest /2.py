import sys
from collections import defaultdict
from math import ceil,floor
input=sys.stdin.readline
def I():return list(map(int,input().split()))
def check(arr):
    diff = arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]!=diff:
            return False
    return True
 
def f():
    if n==2:
        return "YES"
    if a[0]==a[-1]:
        return "NO"
    for i in range(1,n-1):
        val = (a[i-1]+a[i+1])/2
        if ceil(val)!=floor(val):
            continue
        if val!=a[i]:
            temp=a[i]
            a[i]=val
            if check(a):
                return "YES"
            a[i]=temp
            # return "NO"
        
    if check(a[1:]+[a[-1]*2-a[-2]]):
        return "YES"
    return "NO"
 
 
for _ in range(int(input())):
    n = int(input())
    a = I()
    a.sort()
    print(f())