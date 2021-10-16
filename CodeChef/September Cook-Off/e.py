import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    if len(a)>4:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            if i%4==0:
                print("0",a[i])
            elif i%4==1:
                print(a[i],'0')
            elif i%4==3:
                print(-a[i],"0")
            else:
                print("0",-a[i])


