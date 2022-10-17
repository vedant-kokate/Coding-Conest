import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s=input().strip()
    one=s.count('1')
    zero=s.count('0')
    if one%2==0 or zero%2==0:
        print("YES")
    else:
        print("NO") 
    


