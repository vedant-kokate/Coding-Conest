import sys
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    n=int(input())
    a=I()
    b=I()
    b_=[x for _, x in sorted(zip(a, b),reverse=True)]
    ans=1
    max_so_far=b_[0]
    for i in range(1,n):
        if b_[i]>max_so_far:
            ans+=1
            max_so_far=b_[i]
    print(ans)

    # print()