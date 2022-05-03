from decimal import Decimal, getcontext
getcontext().prec = 150
def solution(s):
    d2 = Decimal(2).sqrt()-1
    n = int(s)
    l=[n]
    while l[-1]!=0:
        l.append(int(d2*l[-1]))
    f=[]
    for i in range(len(l)-1):
        F = l[i]**2 + 2*l[i]*l[i+1] + l[i] - l[i+1] - l[i+1]**2
        f.append(F)
    ans = 0
    for i in range(len(f)):
        if i%2:
            ans-=f[i]
        else:
            ans+=f[i]
    ref2 = f 
    return str(ans//2)
test = input()
print(solution(test))