import sys
from itertools import permutations as p
from random import randint as r


n=8
a=[]
for i in range(n):
    a.append(r(1,100))

for arr in list(p(a)):
    max_sum=-1
    this_sum=0
    for i in range(n-1):
        this_sum+=max(0,arr[i+1]-arr[i])
    max_sum=max(max_sum,this_sum)

    a.sort()
    min_diff=10**9
    minpair=()
    for i in range(n-1):
        diff=a[i+1]-a[i]
        if diff<min_diff:
            min_diff=diff
            minpair=(i,i+1)

    ans=[0]*n
    ans[0]=a[minpair[0]]
    ans[-1]=a[minpair[1]]
    minpair=set(minpair)
    last=n-1
    first=0
    i=1
    while True:
        if ans[i]!=0:
            break
        while last in minpair:
            last-=1
        ans[i]=a[last]
        last-=1
        i+=1

        if ans[i]!=0:
            break
        while first in minpair:
            first+=1
        ans[i]=a[first]
        first+=1
        i+=1
    sum2=0
    for i in range(n-1):
        sum2+=max(0,ans[i+1]-ans[i])
    if sum2!=max_sum:
        print(arr,sum2,max_sum)
        