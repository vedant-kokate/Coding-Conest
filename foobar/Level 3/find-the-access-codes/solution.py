
def solution(l):
    n=len(l)
    
    F=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if l[j]%l[i]==0:
                F[i]+=1
    # print(F) 
    S=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if l[j]%l[i]==0:
                S[i]+=F[j]
    # print(S)
    return sum(S)

l= list(map(int,input().split()))
print(solution(l))   
    # Your code here