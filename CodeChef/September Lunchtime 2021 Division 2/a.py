from heapq import heappush, heappop, heapify
import sys
from collections import defaultdict
input=sys.stdin.readline
def f():return list(map(int,input().split()))


def solve(n):
    a=[]
    b=[]
    x=n%4
    if x==1 or x==2:
        print("NO")
        return
    elif x==0:
        for i in range(1,n+1):
            if i%4==0 or i%4==1:
                a.append(i)
            else:
                b.append(i)
    else:
        a=[1,2]
        b=[3]
        for i in range(4,n+1):
            if i%4==0 or i%4==3:
                a.append(i)
            else:
                b.append(i)
    print("YES")
    # print(len(a))
    print(*a)
    b=b[::-1]
    # print(len(b))
    print(*b)

for _ in range(int(input())):
    n=int(input())
    solve(n)
    
