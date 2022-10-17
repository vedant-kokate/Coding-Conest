import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
for _  in range(int(input())):
    n = int(input())
    a=I()
    b=I()
    d1, d2 =[0, 0], [0, 0]
    ans=0
    for i in range(n):
        if a[i]!=b[i]:
            ans+=1
    for i in a:
        d1[i]+=1
    for i in b:
        d2[i]+=1
    print(min(ans,abs(d2[0]-d1[0])+1))
        