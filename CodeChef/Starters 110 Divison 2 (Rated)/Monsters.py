import itertools
import sys

input = sys.stdin.readline
from bisect import bisect_left


def I(): return map(int, input().split())


def solve(h):
    for n in itertools.count(0):
        if (1 << n) - 1 > h:
            return -1
        remain = h - (1 << n) + 1
        # print('remain',remain)
        if remain == 0:
            return n
        if prime_bool[remain]:
            return n + 1


#

# def solve(h, attack, moves, prime_used):
#     print(h, attack, moves)
#     if (h, attack) in mem:
#         return moves + mem[(h, attack)]
#     if h == 0:
#         return moves
#     if h < 0:
#         return 10 ** 10
#     val = solve(h - attack, attack * 2, moves + 1, prime_used)
#     if not prime_used:
#         p = bisect_left(primes, h)
#         if primes[p] > h:
#             p -= 1
#         val = min(val, solve(h - primes[p], attack, moves + 1, True))
#
#     mem[(h, attack)] = val
#     return val


prime_bool = [True] * (10 ** 6 + 100)
primes = []
prime_bool[0] = prime_bool[1] = False
for i in range(2, 10 ** 6 + 100):
    if not prime_bool[i]:
        continue
    primes.append(i)
    for j in range(i * i, 10 ** 6 + 100, i):
        prime_bool[j] = False
mem = {}
ans = 10 ** 10
for _ in range(int(input())):
    ans = 10 ** 10
    h = int(input())
    print(solve(h))
# print(solve(1000000, 1, 1, False))
# print(solve(1000000))
# print(solve(1, 1))
# print(solve(4, 1))
# print(solve(5, 1))
# print(solve(1, 4))
# print(solve(1, 5))
