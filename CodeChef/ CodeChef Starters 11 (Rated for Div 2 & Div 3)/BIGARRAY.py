import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,s=map(int,input().split())
    tot=n*(n+1)//2
    if (tot-n) <= s< tot:
        print(tot-s)
    else:
        print(-1)
