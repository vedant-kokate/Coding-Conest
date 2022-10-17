t=int(input())
for T in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    count=0
    i=0
    b=[a.pop()]
    while a:
        ne=a.pop()
        last=b.pop()
        if last^ne>=lat+ne:
             
    print(b)
    print(sum(b),count)