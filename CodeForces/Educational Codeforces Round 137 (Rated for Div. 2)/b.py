import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    ans=[0]*n 
    ans[0],ans[-1]=1,2
    val=3
    for i in range(1,n-1):
        ans[i]=val
        val +=1
    print(*ans)
