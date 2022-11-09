import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    last = n-1
    last_val = s[last]
    # print(last_val)
    while last>=0 and s[last]==last_val:
        last -=1
    last += 1
    
    find='1'
    ans=0
    for i in range(last):
        if find==s[i]:
            if find=='1':
                find='0'
            else:
                find='1'
            ans+=1
    print(ans)