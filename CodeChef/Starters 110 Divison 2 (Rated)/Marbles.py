import sys

input = sys.stdin.readline
from math import sqrt, ceil, floor
from collections import defaultdict, deque
from heapq import heappop, heappush


def I(): return map(int, input().split())


def solve1(a, b):
    count = 0
    while True:
        # print(a, b)
        if a % b == 0:
            return count
        a += 1
        b -= 1
        count += 1

def solve2(a, b):
    if a<b:
        return 10**10
    count = 0
    while True:
        print(a, b)
        if a % b == 0:
            return count
        a -= 1
        b += 1
        count += 1

for _ in range(int(input())):
    a,b = I()
    v1 = solve1(a,b)
    v2 = solve2(a,b)
    print(min(v1,v2))


# print(solve(1, 1))
# print(solve(4, 1))
# print(solve(5, 1))
# print(solve(1, 4))
# print(solve(1, 5))
