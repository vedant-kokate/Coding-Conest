import sys
from collections import Counter
input=sys.stdin.readline
def I():return list(map(int,input().split()))

for _ in range(int(input())):
    # d=defaultdict(int)
    n=int(input())
    a=I()
    c=Counter(a)
    ans=0
    for v in c.values():
        ans += v*(v-1)//2
    print(ans)
    # print(c.values())
