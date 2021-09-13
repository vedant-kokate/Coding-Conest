import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    cur='right'
    ans=0
    for i,val in enumerate(s):
        if val=='X':
            cur='left'
            break
        elif val=='O':
            cur='right'
            break
    while i<n:
        if s[i]=='X' and cur=='right':
            ans+=1
            cur='left'
        if s[i]=='O' and cur=='left':
            ans+=1
            cur='right'
        i+=1
    print(f"Case #{_+1}: {ans}")

