import sys

input = sys.stdin.readline

from math import ceil
def I(): return list(map(int, input().split()))



def solve():
    global n, target
    total_task = (n-1)//7+1
    max_with_task = total_task * t + l *ceil(total_task/2)
    # print(max)
    if max_with_task >= target:
        days = ceil(target/(2*t +l))
        return n-days
    target -= max_with_task
    n -= ceil(total_task/2)
    # print(n,target)
    n -= ceil(target/l)
    return n
for _ in range(int(input())):
    n, target, l, t  = I()
    print(solve())

