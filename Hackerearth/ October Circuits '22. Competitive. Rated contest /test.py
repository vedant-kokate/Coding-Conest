from random import randint,choice
t=100
name = input().strip()
f=open(f"{name}.txt",'w')
f.write(str(t))
f.write("\n")
for _ in range(t):
    d = []
    d.append(randint(1,5))
    d.append(randint(1,5))
    n = 5
    f.write(str(n))
    f.write("\n")
    a=[randint(1,30)]
    for i in range(n-1):
        a.append(a[-1]+choice(d))
        # a.append(randint(1,n))
    for i in a:
        f.write(str(i)+" ")
    f.write("\n")