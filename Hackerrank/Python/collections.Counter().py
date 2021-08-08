# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x=int(input())

shoes=Counter(list(map(int,input().split())))
n=int(input())
a=[]
for i in range(n):
    temp1,temp2=map(int,input().split())
    a.append((temp2,temp1))
# a.sort(reverse=True)
# print(shoes)
# print(a)
ans=0
for prize,size in a:
    if size in shoes and shoes[size]>0:
        ans+=prize
        shoes[size]-=1
print(ans)
    