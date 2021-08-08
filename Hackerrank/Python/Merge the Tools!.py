S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    ans=""
    for i in part:
        if i not in d:
            d[i]=1
            ans+=i
    print(ans)

    # print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))