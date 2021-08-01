import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))
for _ in range(int(input())):
    n=int(input())
    a=I()
    
    a.sort()
    ans=0
    i=1
    j=0
    # print(a)
    while i<n:
        if a[i]!=a[i-1]:
            j=i 
            ans+=i 
        else:
            ans+=j
        i+=1
    print(ans*2)
