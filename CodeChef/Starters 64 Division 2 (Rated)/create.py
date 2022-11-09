from random import randint

f=open('test1.txt','w')
t=10
f.write(str(t))
f.write("\n")

for _ in range(t):
    n = randint(1, 10)
    f.write(str(n))
    f.write("\n")
    for i in range(n):
        f.write(str(randint(1,20))+" ")
    f.write("\n")