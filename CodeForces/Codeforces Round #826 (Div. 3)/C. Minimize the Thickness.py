import sys
input=sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    sum_=0
    ans=[]
    for i in range(n):
        sum_ += a[i]
        j,k=i+1,i+1
        sum2=0
        flag=True
        max_so_far=i+1
        while k<n :
            sum2+=a[k]
            if sum2>sum_:
                flag=False
                break 
            if sum2==sum_:
                max_so_far = max(max_so_far,k-j+1)
                j=k+1
                sum2=0
            k+=1
        if flag and (sum2==0 or sum2==sum_):
            ans.append(max_so_far)
    print(min(ans))