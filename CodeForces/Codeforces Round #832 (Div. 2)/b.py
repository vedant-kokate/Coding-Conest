import sys
input=sys.stdin.readline
from collections import defaultdict
from math import gcd
def I():return list(map(int,input().split()))
import re 
def check(s):
    x=re.search("B[A-Z]*A[A-Z]*N",s)
    # print(x)
    return x

for _ in range(int(input())):
    n=int(input())
    a=['B','A','N']*n 
    ans=[]
    i, j = 0, len(a)-1
    # if n==2:
    #     print(1)
    #     print(1,4)
    #     continue
    while i<j :
        while j>=0 and a[j]!='N':
            j-=1
        if j<0:
            break
        while i<len(a) and a[i]!='B':
            i+=1
        if i>=len(a):
            break
        a[j]=a[i]
        a[i]='N'
        ans.append((i+1,j+1))
        i+=1
        j-=1
        # print("".join(a))
        if check("".join(a))==None:
            break
        

    print(len(ans))
    for i,j in ans:
        print(i,j)
