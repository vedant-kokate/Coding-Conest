import sys
input=sys.stdin.readline
from math import sqrt
from collections import defaultdict
from random import randint as r
def I():return list(map(int,input().split()))

def factors(n):
    a=set()
    for i in range(2,n+1):
        if n%i==0:
            a.add(n*i)
    return a
f_input= open("input.txt",'w')
f_output= open("output.txt",'w')
t=r(500,1000)
f_input.write(f"{t}\n")
for T in range(t):
    n=r(1,10**7)
    k=r(1,10**5)
    f_input.write(f"{n} {k}\n")
f_input.close()
print("done")
# t=1

# for _ in range(t):
#     n=r(2,20)
#     k=r(1,5)
#     print(n,k)
#     f_input.write(f"{n} {k}\n")
#     stack=[(n,0)]
#     ans=set()
#     ans.add(n)
#     while stack:
#         num,dep=stack.pop()
#         if dep<k:
#             for i in range(2,num+1):
#                 if num%i==0 and num*i not in ans :
#                     ans.add(num*i)
#                     stack.append((num*i,dep+1))
#     f_output.write(f"{sum(ans)}\n")

