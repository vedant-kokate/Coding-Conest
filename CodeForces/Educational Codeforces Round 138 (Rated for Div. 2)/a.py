import sys
input = sys.stdin.readline
def I():return list(map(int,input().split()))
for _  in range(int(input())):
    n,m = I()
    for q in range(m):
        x,y=I()
    if m<n:
        print("YES")
    else:
        print("NO")
