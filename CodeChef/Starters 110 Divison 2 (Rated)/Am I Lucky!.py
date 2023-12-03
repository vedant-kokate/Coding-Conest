import sys

input = sys.stdin.readline
from math import sqrt, ceil, floor
from collections import defaultdict, deque
from heapq import heappop, heappush


def I(): return map(int, input().split())


def solve(n,x,k):
    boys = x%k
    girls = (n - boys)%k
    min_ = min(boys,girls)
    boys -=min_
    girls -= min_
    return boys + girls



for _ in range(int(input())):
    n,x, k = I()

    print(solve(n,x,k))


# print(solve(1, 1))
# print(solve(4, 1))
# print(solve(5, 1))
# print(solve(1, 4))
# print(solve(1, 5))
