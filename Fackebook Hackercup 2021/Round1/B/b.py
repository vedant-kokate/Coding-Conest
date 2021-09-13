import sys
input=sys.stdin.readline
from collections import defaultdict
def f():return list(map(int,input().split()))

for _ in range(int(input())):
    n,m,a,b=f()
    fastest_travel=n+m-1
    if a<fastest_travel or b<fastest_travel:
        print(f"Case #{_+1}: Impossible")
    else:
        print(f"Case #{_+1}: Possible")
        mat=[[1]*m for i in range(n)]
        mat[0][0]=a-fastest_travel+1
        mat[0][-1]=b-fastest_travel+1
        for i in mat:
            print(*i)

