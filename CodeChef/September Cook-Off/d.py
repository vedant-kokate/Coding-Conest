import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    p=input().strip()
    if p==s:
        print("YES")
    elif p.count('1')==0 or p.count('0')==0:
        print("NO")
    else:
        print('YES')
