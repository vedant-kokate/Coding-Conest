import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    a,b=I()
    if b-a>=a:
        print("YES")
    else:
        print("NO")



