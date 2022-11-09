import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s=input().strip()
    last=""
    ans = 0
    for i in s:
        if not last:
            last=i
        else:
            if last>i:
                ans+=1
                last=i 
            else:
                last=max(last,i)
    print(ans)



