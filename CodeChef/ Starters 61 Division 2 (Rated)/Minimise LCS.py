import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s1=input().strip()
    s2=input().strip()
    d1,d2=defaultdict(int),defaultdict(int)
    for ch in s1:
        d1[ch]+=1
    for ch in s2:
        d2[ch]+=1
    ans=0
    for key in d1:
        ans=max(ans,min(d2[key],d1[key]))
    print(ans)


