import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    temp=input().strip()
    s=[]
    s[:]=temp
    
    a=I()
   
    left = -1
    for i in range(n):
        if s[i]=='1':
            if left!=-1 and a[left]>a[i]:
                s[i]='0'
                s[left]='1'
                left=i
        else:
            left=i
    ans=0
    for i in range(n):
        if s[i]=='1':
            ans += a[i]
    print(ans)

