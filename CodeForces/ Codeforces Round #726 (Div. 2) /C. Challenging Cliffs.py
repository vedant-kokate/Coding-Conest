import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
for _  in range(int(input())):
    n=int(input())
    a=I()
    a.sort()
    min_diff=10**9
    minpair=()
    for i in range(n-1):
        diff=a[i+1]-a[i]
        if diff<min_diff:
            min_diff=diff
            minpair=(i,i+1)

    ans=[0]*n
    ans[0]=a[minpair[0]]
    ans[-1]=a[minpair[1]]
    minpair=set(minpair)
    last=n-1
    first=0
    i=1
    while True:
        if ans[i]!=0:
            break
        while last in minpair:
            last-=1
        ans[i]=a[last]
        last-=1
        i+=1

        if ans[i]!=0:
            break
        while first in minpair:
            first+=1
        ans[i]=a[first]
        first+=1
        i+=1
    print(*ans)


