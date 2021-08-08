import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=f()
    ans=0
    for i in a:
        ans^=i
    if ans==0 :
        print("Second")
    else:print("First")
    