import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
from math import ceil
for _ in range(int(input())):
    N=int(input())
    a=f()
    ans=0
    cap=min(a)*2-1
    for i in a:
        if i>cap:
            # print(i)
            ans += ceil(i/cap)-1
    print(ans)
