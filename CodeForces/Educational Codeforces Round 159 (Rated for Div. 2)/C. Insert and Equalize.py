import sys

input = sys.stdin.readline

import math
def I(): return list(map(int, input().split()))



def solve():
    max_ = max(a)
    gcd = -10**11
    for i in a:
        if i==max_:
            continue
        if gcd ==-10**11:
            gcd = max_ - i
        else:
            gcd = math.gcd(gcd,max_-i)
    ans = 0
    for i in a:
        if i==max_:
            continue
        ans += (max_-i)//gcd
    cur = max_ - gcd 
    while cur in a:
        cur -= gcd 
    ans += (max_-cur)//gcd 
    return ans
    
for _ in range(int(input())):
    n = int(input())
    a = set(I())
    print(solve())

