import sys
input = sys.stdin.readline
from collections import defaultdict
def I():return list(map(int,input().split()))
n, m =I()
d=defaultdict(set)
for _ in range(m):
    x,*a=I()
    for i in a:
        d[i].add(_)
for i in range(1,n+1):
    for j in range(1,i):
        if len(d[i].intersection(d[j]))==0:
            # print(i,j)
            print("No")
            exit()

print("Yes")



