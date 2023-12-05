import sys
input = sys.stdin.readline
def I(): return list(map(int, input().split()))

def solve():
    one_count, zero_count = 0,0
    for i in s:
        if i=='0':
            return "YES"
    return "NO"


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve())
