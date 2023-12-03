import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7

def I(): return map(int, input().split())


def solve(a_turn, tot_l):
    if (a_turn, l - tot_l) in mem:
        return mem[(a_turn, l - tot_l)]
    val = 0
    if a_turn and tot_l + 4 >= l:
        val += 1
    if tot_l >= l:
        return 0
    val += solve(a_turn ^ 1, tot_l + 1) + solve(a_turn, tot_l + 2) + solve(a_turn, tot_l + 3) + solve(a_turn, tot_l + 4)
    val %= mod
    mem[(a_turn, l - tot_l)] = val
    return val


mem = {}

for _ in range(int(input())):
    l = int(input())
    print(solve(1, 0))
