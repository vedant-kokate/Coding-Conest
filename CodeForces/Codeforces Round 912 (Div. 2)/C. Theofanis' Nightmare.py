import sys

input = sys.stdin.readline


def I(): return list(map(int, input().split()))


def solve():
    b = [0] * n
    b[0] = 1
    cur = 1
    sum_a = [0] * n
    sum_a[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        sum_a[i] = a[i] + sum_a[i + 1]

    for i in range(1, n):
        if sum_a[i] >= 0:
            cur += 1
        b[i] = cur
    # print(sum_a)
    # print(b)
    for i in range(n):
        a[i] *= b[i]
    # print(a)
    tot = sum(a)
    print(tot)
    # return tot

    # max_ = 0

    # sum_a[-1] = a[-1]

    # # print(sum_a)
    # b = [0]*n
    # tot = 0
    # for i in range(n):
    #     max_ += a[i]
    #     tot += (i + 1) * a[i]
    #
    # for i in range(n - 1, -1, -1):
    #     if tot - sum_a[i] > tot:
    #         tot -= sum_a[i]
    #         b[i]-=1
    # print(b)
    # count = 1
    # for i in range(n):
    #     b[i] += count
    #     count = b[i]
    #     count+=1
    # print(b)
    # if b[0] == 0:
    #     print(max_)
    #     return
    # print(tot)


for _ in range(int(input())):
    n = int(input())
    a = I()
    solve()

# 4
# 6
# 1 -3 7 -6 2 5
# 4
# 2 9 -5 -3
# 8
# -3 -4 2 -5 1 10 17 23
# 1
# -830
