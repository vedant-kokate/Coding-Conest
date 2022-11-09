import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    s1,s2=0,0
    for i in a:
        if i>0:
            s1+=i 
        else:
            s2+=i 
    s2 = -s2
    print(max(s1,s2)-min(s1,s2))
    
