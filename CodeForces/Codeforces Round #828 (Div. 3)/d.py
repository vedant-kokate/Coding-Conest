import sys
input=sys.stdin.readline
from collections import defaultdict
from math import log2
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a=I()
    target = n
    for i in range(n):
        while a[i]%2==0:
            target -=1
            a[i]//=2
    if target<=0:
        print(0)
        continue
    # print(target,'tar')
    p=int(log2(n))
    count = 0
    for P in range(p,0,-1):
        target-=P
        count +=1
        if target<=0:
            break
    # print(target,count)
    if target<=0:
        print(count)
    else:
        print(-1)
    # print(target,count)
    

            
