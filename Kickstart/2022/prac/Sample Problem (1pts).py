import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    n,m=f()
    c=f()
    ans = sum(c)%m
    
        
    print(f"Case #{_+1}: {ans}")