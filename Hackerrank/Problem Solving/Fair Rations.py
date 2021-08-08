import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))

n=int(input())
a=f()

if sum(a)%2==1:
    print("NO")
    exit()

i=0
ans=0
while i<n-1:
    if a[i]%2==1:
        ans+=2
        a[i]+=1
        a[i+1]+=1
    i+=1
print(ans)