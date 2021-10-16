import sys
from collections import defaultdict
import math
input=sys.stdin.readline
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    l,r=f()
    if l%3==0:
        print((r//3)-(l//3) + 1) 
    else:
        print(((r // 3) - (l // 3))) 
    

    