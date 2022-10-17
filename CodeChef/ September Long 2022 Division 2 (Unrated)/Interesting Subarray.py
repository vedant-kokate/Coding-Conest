import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    min_,max_=min(a),max(a)
    l=[min_*min_,min_*max_,max_*max_]
    print(min(l),max(l))