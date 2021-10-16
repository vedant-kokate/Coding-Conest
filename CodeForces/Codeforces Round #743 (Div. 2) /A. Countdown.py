import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    N=int(input())
    n=int(input())
    n=str(n)
    l=[]
    l[:0]=n
    ans=0
    cur=l.pop()
    ans+=int(cur)
    # print(l)
    
    while l:
        cur=l.pop()
        cur=int(cur)
        if cur!=0:
            ans+=cur+1
    print(ans)