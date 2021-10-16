# Code by Vedant Kokate
import sys
input=sys.stdin.readline

min_val=-1

for _ in range(int(input())):
    N = int(input())
    ans = [[min_val for j in range(N)] for i in range(N)]
    if N % 2 != 0:
        for i in range(N):
            ans[-1][i]=1
            ans[i][-1] = 1
        ans[N - 1][N - 1] = -1

    for i in ans:
        for j in i:
            print(j,end=" ")
        print()


