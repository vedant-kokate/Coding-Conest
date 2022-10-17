import sys
input = sys.stdin.readline
from math import gcd
def I():return list(map(int,input().split()))
def solve(a,n):
    b=a.copy()+[a[-1]]
    for i in range(n):
        gcd_=gcd(b[i], b[i+1])
        if gcd_!=a[i]:
            if a[i]%gcd_==0:
                rem = a[i]//gcd_
            else:
                rem = a[i]
            b[i+1]*=rem

    for i in range(n):
        gcd_=gcd(b[i], b[i+1])
        if gcd_!=a[i]:
         
            return "NO"
    
    return "YES"
    
for _  in range(int(input())):
    n = int(input())
    a=I()
    print(solve(a,n))
    

    

# 4 6  5  8  2 
# 4 12 30 40 8 2