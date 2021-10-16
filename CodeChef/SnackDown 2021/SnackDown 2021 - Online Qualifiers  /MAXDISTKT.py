import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    temp=I()

    b=[]
    for i,val in enumerate(temp):
        b.append((val,i))
    b.sort()
    # print(b)
    a=[-1]*n

    count = 0
    for val,i in b:
        if count>=val:
            count=val-1
        a[i] = count
        count+=1
    print(*a)

    # c=[a[i]%temp[i] for i in range(n)]