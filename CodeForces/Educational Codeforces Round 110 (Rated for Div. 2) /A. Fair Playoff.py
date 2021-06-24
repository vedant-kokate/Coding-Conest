import sys
input = sys.stdin.readline

for _  in range(int(input())):
    a,b,c,d=map(int,input().split())
    if min(a,b)>max(c,d) or min(c,d)>max(a,b):
        print("NO")
    else:
        print("YES")