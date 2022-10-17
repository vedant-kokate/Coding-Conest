import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
def I():return list(map(int,input().split()))

def maxSubArraySum(a, size): 
    max_so_far = -10**10
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

mod=10**9+7
for _ in range(int(input())):
    n=int(input())
    a=I()
    m=int(input())
    b=I()
    sum_=0
    for i in b:
        if i>0:
            sum_+=i 
    a.append(sum_)
    ans1=maxSubArraySum(a, len(a))
    a.pop()
    a.insert(0, sum_)
    ans2=maxSubArraySum(a, len(a))
    print(max(ans1,ans2))


