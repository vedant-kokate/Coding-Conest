from collections import defaultdict
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if all(b[0] == i for i in b):
        start = 0
    else:
        index = defaultdict(list)
        mini =10**9
        for i in range(n):
            index[(a[0] + b[i]) % n].append((i, i))
            mini = min(mini, (a[0] + b[i])%n)

        start = find_index(a, b, index[mini], n)

    ans = []
    for arr, brr in zip(a, b[start:] + b[:start]): ans.append((arr + brr) % n)
    print(*ans)



def find_index(a, b, indexes, n):
    iter = 1
    while True:
        print(indexes)
        print()
        if len(indexes) == 1: return indexes[0][0]
        if iter == n: return indexes[0][0]
        else:
            index = defaultdict(list)
            mini = 10**9
            for start, i in indexes:
                next_index = i + 1
                if next_index == n: next_index = 0

                index[(a[iter] + b[next_index]) % n].append((start, next_index))
                mini = min(mini, (a[iter] + b[next_index])%n)

            indexes = index[mini]
            iter += 1

for t in range(int(input())):
    solve()