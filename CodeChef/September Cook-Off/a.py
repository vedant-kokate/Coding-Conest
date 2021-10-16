import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))
for _ in range(int(input())):
    n=int(input())
    a=I()
    even=[]
    odd=[]
    for i in a:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    if len(odd)==0 or len(even)==0:
        print(-1)
    else:
        print(*odd,*even)

