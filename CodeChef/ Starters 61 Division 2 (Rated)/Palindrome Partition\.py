import sys
input=sys.stdin.readline
from math import sqrt
# from random import randint
from collections import defaultdict
from heapq import heappop,heappush
def I():return list(map(int,input().split()))

for _ in range(int(input())):
# for _ in range(10):
    n = int(input())
    s=input().strip()
    if s.count('0') == 0 or s.count('1') == 0:
        print(-1)
    elif s!=s[::-1]:
        print(1)
        print(2*n)
    else:
        ans=[]
        for i in range(2,len(s)):
            s1=s[:i]
            s2=s[i:]
            if s1!=s1[::-1] and s2!=s2[::-1]:
                ans = [i,2*n-i]
                # print(s1,s2)
                break
        print(2)
        print(*ans)
