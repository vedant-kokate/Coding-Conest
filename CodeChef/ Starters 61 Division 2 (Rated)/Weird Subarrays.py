import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a=I()
    ans=n
    if n>1:
        ans += n-1
    stack=[]
    for i,val in enumerate(a):
        if not stack:
            stack.append(val)
        else:
            if len(stack)==1:
                if val>stack[-1]:
                    stack.append(val)
                else:
                    stack.append(-val)
            else:
                if -val>stack[-1]:
                    stack.append(-val)
                elif val>stack[-1]:
                    stack.append(val)
                else:
                    tot = len(stack)*(len(stack)+1)//2 - 2*len(stack)+1
                    if tot>0:
                        ans += tot 
                    stack=[stack.pop()]
                    if val>stack[-1]:
                        stack.append(val)
                    else:
                        stack.append(-val)
    tot = len(stack)*(len(stack)+1)//2 - 2*len(stack)+1
    if tot>0:
        ans += tot
  
    print(ans)