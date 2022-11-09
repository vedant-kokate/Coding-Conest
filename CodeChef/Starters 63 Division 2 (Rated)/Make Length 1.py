import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))
# from random import randint
# for _ in range():
def f():
    i=0
    if n==1:
        return "YES"
    while i<n:
        if s[i]=='1':
            # print(i)
            count=0
            while i<n and s[i]=='1':
                i+=1
                count+=1
            # print(count,i)
            if count%2:
                return "NO"
            i-=1
        i+=1
    return "YES"
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(f())
        
