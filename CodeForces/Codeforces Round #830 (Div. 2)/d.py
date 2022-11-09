import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd
def I():return list(map(int,input().split()))

d={}
query=defaultdict(lambda:1)
for _ in range(int(input())):
    q,num=input().split()
    num=int(num)
    if q=='+':
        d[num]=True
    else:
        start=query[num]
        while start*num in d:
            start+=1
        print(start*num)
        query[num]=start

