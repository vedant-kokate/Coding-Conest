import sys
from collections import defaultdict
input=sys.stdin.readline
def I():return list(map(int,input().split()))

a = []
substring=set()
for _ in range(int(input())):
    s=input().strip()
    # a.append()
    for i in range(1,len(s)+1):
        substring.add(s[:i])
# print(substring)
mod=10**9+7
ans=0
for s in substring:
    n=len(s)
    i,j=0,0
    while i<n and j<n:
        while i<n and s[i]!='b':
            i+=1
        if i==n:
            break
        j=i+1
        while j<n and s[j]!='b':
            j+=1
        if j==n:
            break
        ans += 1
        i=j
print(ans)
# print(dp[-1])

