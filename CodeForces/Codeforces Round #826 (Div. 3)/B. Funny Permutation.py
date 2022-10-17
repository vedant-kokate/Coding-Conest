import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    if n%2:
        if n<5:
            print(-1)
        else:
            a = [n,n-1]
            print(*a,*list(range(1,n-1)))
        pass 
    else:
        a=list(range(1,n+1))
        print(*a[::-1])
