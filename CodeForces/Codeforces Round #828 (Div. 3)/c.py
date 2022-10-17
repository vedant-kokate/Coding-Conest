import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n, c = input().split()
    n=int(n)
    s=input().strip()
    s+=s
    last_color=-1
    ans=0
    for i,val in enumerate(s):
        # print(i,last_color)
        if val=='g':
            if last_color!=-1:
                ans=max(ans,i-last_color)
                last_color=-1
  
        elif val==c and last_color==-1:
            last_color=i
    print(ans)
            
