import sys
from collections import defaultdict
from math import ceil,floor
input=sys.stdin.readline
def I():return list(map(int,input().split()))
def f(l, r):
  
    res = 0; 
    l += n
    r += n
      
    while l < r :
        if (l & 1) :
            res += tree[l]; 
            l += 1
        
        if (r & 1) :
            r -= 1
            res += tree[r]; 
              
        l >>= 1
        r >>= 1
      
    return res; 

n,q=I()
a=I()
tree = [0]*n+a 
for i in range(n-1,-1,-1):
    tree[i] = tree[i<<1] + tree[i<<1|1] 

for _ in range(q):
    l,r=I()
    print(f(l-1,r))