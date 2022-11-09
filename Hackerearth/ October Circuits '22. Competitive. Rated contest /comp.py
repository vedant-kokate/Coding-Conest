import sys
from collections import defaultdict
input=sys.stdin.readline
def I():return list(map(int,input().split()))
def check(arr):
    # print(arr)
    arr.sort()
    diff = arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]!=diff:
            return False
    return True

def f():
    d=defaultdict(int)
    for i in range(1,n):
        diff=a[i]-a[i-1]
        d[diff]+=1
    # print(d)
    if len(d)>3:
        return "NO"
    if a[-1]==a[0]:
        return "NO"
    for change in d:
        # print(change)
        b=a.copy()
        # print(a,a[1:]+[a[-1]+change])
        
        if check(a[1:]+[a[-1]+change]):
            return "YES"
        # print(b)
        for i in range(1,n):
            if b[i]-b[i-1]!=change:
                b[i]=b[i-1]+change
                break
        if check(b):
            return "YES"
    return "NO"
def sol2():
    d=defaultdict(int)
    for i in range(1,n):
        diff=a[i]-a[i-1]
        d[diff]+=1
    if len(d)==1:
        if d[0]>0:
            return("NO")
        else:
            return("YES")
    elif len(d)<=3:
        return("YES")
    else:
        return("NO")
from random import randint
for _ in range(100):
    n = randint(10, 100)
    a=[]
    for i in range(n):
        a.append(randint(1,n))
    a.sort()
    ans1=f()
    ans2=sol2()
    if ans1!=ans2:
        print(ans1,ans2)
        print(n)
        print(a)
        exit()
print("Sucess")

# print(dp[-1])

