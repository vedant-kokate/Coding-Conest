import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    s=input().strip()
    d={}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = s[i]
        a[i]=d[a[i]]
    s2="".join(a)
    if s2==s:
        print("YES")
    else:
        print("NO")

