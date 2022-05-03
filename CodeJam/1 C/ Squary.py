import sys
input=sys.stdin.readline
from math import floor,ceil
from heapq import heapify,heappop, heappush
from collections import defaultdict,deque
def f():return list(map(int,input().split()))
# sq= []
# for i in range(1,10**4):
#     sq.append(i*i)
for _ in range(int(input())):
    flag = True
    n,k = f()
    l = f()
    s2 = 0
    for i in l:
        s2 +=i*i
    s1=sum(l)
    if s2==0:
        print(f"Case #{_+1}: 0")
    elif s1!=0:
        x = (s2-s1**2)/(2*s1)
        if floor(x)==ceil(x):
            print(f"Case #{_+1}: {int(x)}")
        else:
            print(f"Case #{_+1}: IMPOSSIBLE")
    else:
        print(f"Case #{_+1}: IMPOSSIBLE")
        # print(x)
    # if flag:
        # print(f"Case #{_+1}: IMPOSSIBLE")
    