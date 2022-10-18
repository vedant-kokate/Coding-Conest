import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    left = 10-n 
    ans=1
    for i in range(2,left+1):
        ans*=i 
    for i in range(2,left+1-2):
        ans//=i 
    ans//=2
    print(ans*6)
