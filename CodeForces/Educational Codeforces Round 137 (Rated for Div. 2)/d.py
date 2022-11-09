import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

n = int(input())
temp=input().strip()

s=[]
s[:]=temp
one_idx=-1
for i in range(n):
    if s[i]=='1':
        one_idx=i
        break

if one_idx==-1:
    print(0)
    exit()

zero=-1
for i in range(one_idx,n):
    if s[i]=='0':
        zero = i
        break

if zero==-1:
    print(temp)
    exit()
# print("h")
l=n-zero
# print(l,n,zero)
max_=0
n1=int(temp,2)
for i in range(one_idx,zero):
    n2=int(temp[i:i+l],2)
    max_=max(max_,n2|n1)
ans=bin(max_)[2:]
print('0'*(n-len(ans))+ans)

