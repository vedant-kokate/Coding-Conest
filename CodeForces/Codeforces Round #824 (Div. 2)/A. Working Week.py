import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    N=int(input())
    print(N//3-2)