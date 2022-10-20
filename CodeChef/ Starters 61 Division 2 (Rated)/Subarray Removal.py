import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a=I()
    ans=0 
    stack=[]
    for i,val in enumerate(a):
        if not stack:
            stack.append(val)
        else:
            if val^stack[-1]==1:
                ans+=1
                stack.pop()
            else:
                stack.append(val)
    c=stack.count(1)
    print(ans+c//3)