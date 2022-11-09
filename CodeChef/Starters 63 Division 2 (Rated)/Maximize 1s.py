import sys
input=sys.stdin.readline
from math import sqrt,ceil,floor
from collections import defaultdict
def I():return list(map(int,input().split()))
# def SubArraySum(arr, n ):
#     result = 0
#     for i in range(0, n):
#         if arr[i]=='1':
#             result += ((i+1) * (n-i))
#     return result
for _ in range(int(input())):
    s = input().strip()
    n=len(s)
    val = [0]*n
    for i in range(n):
        val[i]=(i+1) * (n-i)
    # print(val)
    val_til_now = 0
    max_val = -1
    sub=[-1,-1] 
    count=0
    for i in range(n):
        count+=1
        if s[i]=='1':
            val_til_now-=val[i]
        else:
            val_til_now+= val[i]
        if val_til_now<=0:
            val_til_now=0
            count=0
        elif val_til_now>max_val:
            max_val=val_til_now
            sub=[i-count+1,i]
    # print(sub)

   
    l=[]
    l[:]=s
    if sub!=[-1,-1]:
        for i in range(sub[0],sub[1]+1):
            if l[i]=='0':
                l[i]='1'
            else:
                l[i]='0'
    ans=0
    for i in range(n):
        if l[i]=='1':
            ans+=val[i]
    print(ans)