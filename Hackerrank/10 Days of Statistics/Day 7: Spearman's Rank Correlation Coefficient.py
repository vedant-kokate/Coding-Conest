n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

def get_rank(x):
    x_rank=dict((x,i+1) for i,x in enumerate(sorted(x)))
    return [x_rank[i] for i in x]


rx = get_rank(x)
ry = get_rank(y)

d = [(rx[i] -ry[i])**2 for i in range(n)]
ans = 1 - (6 * sum(d)) / (n * (n*n - 1))

print(round(ans,3))