import sys

input = sys.stdin.readline


def I(): return list(map(int, input().split()))


def check(a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if mat[i][j] != a[i] | a[j]:
                return False
    return True


def solve():
    a = [(1 << 30) - 1] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a[i] &= mat[i][j]
            a[j] &= mat[i][j]
    flag = check(a)
    # print(mat)
    # print(a)
    if not flag:
        print("NO")
        return
    print("YES")
    print(*a)


for _ in range(int(input())):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(I())
    solve()
