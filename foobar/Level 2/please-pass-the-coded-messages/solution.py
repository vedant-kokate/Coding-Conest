from itertools import combinations
def solution(l): 
    def list_to_int(L):
        if len(L)==0:return 0
        L.sort(reverse=True)
        L2=[str(x) for x in L]
        return int("".join(L2))
    n=len(l)

    ans = 0
    for i in range(3):
        for comb in list(combinations(l, n-i)):
            if sum(comb)%3==0:
                temp =list_to_int(list(comb))
                if temp>ans:
                    ans=temp
    return ans

l=list(map(int,input().split()))
print(solution(l))