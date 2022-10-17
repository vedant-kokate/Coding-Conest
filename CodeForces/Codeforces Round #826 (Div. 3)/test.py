from random import randint
f=open('input.txt','w')
tot=2*10**5
t=randint(1, 10**4)
f.write(str(t)+"\n")
for T in range(t):
    n=randint(1, max(min(tot,10**5),1))
    f.write(str(n)+"\n")
    tot -=n
    for i in range(n):
        x=randint(1, n)
        f.write(str(x)+" ")
    f.write("\n")
