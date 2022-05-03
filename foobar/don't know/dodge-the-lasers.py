from math import floor
def solution(s):
    # global ref2
    n = int(s)
    l=[n]
    # alpha =sqrt(2)
    # beta = alpha/(alpha-1)

    while l[-1]!=0:
        l.append(floor(frac_sqrt_2_till_100*l[-1]//(10**100)))
    # print(l)17677669529663689274023919016659124224
        #     17677669529663689274023919016659124224
    # print(l)
    f=[]
    for i in range(len(l)-1):
        F = floor(l[i]*l[i+1] + l[i]*(l[i]+1)/2 - l[i+1]*(l[i+1]+1)/2)
        f.append(F)
    ans = 0
    for i in range(len(f)):
        if i%2:
            ans-=f[i]
        else:
            ans+=f[i]
    # ref2 = f 
    return str(ans)
frac_sqrt_2_till_100 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
print(solution('1234564'))