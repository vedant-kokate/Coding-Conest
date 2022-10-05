import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
N,M=I()
d=[]
ans=(-1,-1)
for d in range(1,10):
    last=0
    
    for n in range(1,N+1):
        rem=(d%M)*(pow(10,n-1,M))+last
        rem%=M
        last=rem 
        if rem==0:
            ans=max(ans,(n,d))
if ans==(-1,-1):
    print(-1)
else:
    print(str(ans[1])*ans[0])


