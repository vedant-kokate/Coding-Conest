import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
for _  in range(int(input())):
    n=int(input())
    a=I()
    s=sum(a)
    if s/n==1:
        print(0)
    elif s>n:
        print(s-n)
    else:
        print(1)