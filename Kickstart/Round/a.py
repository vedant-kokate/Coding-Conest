import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    a=[10**10]*len(s)
    last=-1
    for i in range(n):
        if s[i]=='1':            
            last=i
        if last!=-1 :
            
            a[i]=i-last
        
    # print(a)
    last=-1
    for i in range(n-1,-1,-1):
        # print(i,last)
        if s[i]=='1':
            last=i
        if last!=-1 :
            a[i]=min(last-i,a[i])
        
    print(f"Case #{_+1}: {sum(a)}")