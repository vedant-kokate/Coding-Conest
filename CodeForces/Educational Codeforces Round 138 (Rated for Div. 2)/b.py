import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
for _  in range(int(input())):
    n = int(input())
    if n==1:
        a = int(input())
        b = int(input())
        print(a)
        continue
    a = I()
    b = I()
    i, j = 0,n-1
    ans=0
    while i<=j:
        if b[i]<b[j]:
            ans+=a[i]
            a[i+1] += b[i]
            i+=1
        else:
            ans += a[j]
            a[j-1] += b[j]
            j-=1
    print(ans)

            

    