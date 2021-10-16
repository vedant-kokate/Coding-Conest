import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().strip().split()))

for _ in range(int(input())):
    s=input().strip()
    a=[]
    a[:0]=s
    ans=1
    for i in range(1,len(s)):
        if a[i]!=a[i-1]:
            ans+=1
    if s[0]=='1':
        print(ans-1)
    else:
        print(ans)

