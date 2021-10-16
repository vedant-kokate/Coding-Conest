import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    a,b,c=I()

    if a==7 or b==7 or c==7:
        print("YES")
    else:
        print("NO")