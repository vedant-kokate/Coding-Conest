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
    a1=set(a)
    for change in d:
        for first in [a[0],a[1]]:
            b1=set()
            for i in range(n):
                b1.add(first+change*i)
            # print(b1)
            if len(b1-a1)==1 and len(a1-b1)<=2:
                return "YES"
    return "NO"
 
for _ in range(int(input())):
    n = int(input())
    a = I()
    a.sort()
    d=defaultdict(int)
    for i in range(1,n):
        diff=a[i]-a[i-1]
        if i-2>=0:
            d[a[i]-a[i-2]]+=1
        d[diff]+=1
    if len(d)==1:
        if d[0]>0:
            print("NO")
        else:
            print("YES")
    elif len(d)<=10:
        ans1=f()
        print(ans1)    # print(a)
    else:
        print("NO")