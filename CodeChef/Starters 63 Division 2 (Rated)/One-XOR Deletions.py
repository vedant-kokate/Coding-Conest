import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = I()
    d = defaultdict(int)
    for i in a:
        if i%2==0:
            d[i]+=1
            d[i+1]+=1
        else:
            d[i]+=1
    print(n-max(d.values()))
        
