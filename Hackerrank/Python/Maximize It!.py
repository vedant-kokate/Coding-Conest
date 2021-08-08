import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))
from itertools import product

K,M=I()

mat=[]
for i in range(K):
    temp=I()
    mat.append(temp[1:])

ans=0
for nums in list(product(*mat)):
    ans=max(ans,sum(i*i for i in nums)%M)
print(ans)
