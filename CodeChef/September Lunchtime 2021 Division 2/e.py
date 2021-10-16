from collections import defaultdict
d=defaultdict(list)
lim=100
p=[True]*lim
for i in range(2,lim):
    if p[i]:
        for j in range(i*2,lim,i):
            p[j]=False
            d[j].append(i)

print(d)

