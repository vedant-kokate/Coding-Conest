import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))
def f(x,y):
    # print(x,y)
    x-=97
    y-=97
    return (x-y)%26,(y-x)%26
for _ in range(int(input())):
    n = int(input())
    s1=input().strip()
    s2= input().strip()
    a=[]
    b=[]
    ans= 0
    ans2=0
    for i in range(n):
        a.append(f(ord(s1[i]),ord(s2[i])))
        ans+=a[i][0]
        ans2+=a[i][1]
        b.append(sum(a[i]))
    # print(ans%26,ans2%26)
    print(min(ans%26,ans2%26))