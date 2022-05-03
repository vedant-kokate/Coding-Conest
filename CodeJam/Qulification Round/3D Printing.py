import sys
input=sys.stdin.readline
def f():return list(map(int,input().split()))
for _ in range(int(input())):
    col = [[],[],[],[]]
    for i in range(3):
        temp =f()
        for j in range(4):
            col[j].append(temp[j])
    # print(col)
    ans = [min(i) for i in col]
    # print(ans)
    print(f"Case #{_+1}:",end=" ")
    if sum(ans)<10**6:
        print("IMPOSSIBLE")
        continue

    for i in range(3):
        if sum(ans)>10**6:
            ans[i] -= min(ans[i],sum(ans)-10**6)
    print(*ans)