def solution(s):
    n=len(s)
    # print(n)
    for i in range(1,n+1):
        part=s[:i]
        j=i
        while part==s[j:j+i]:
            j+=i
        # print(i,j)
        if j==n:
            return n//i

S=input().strip()
print(solution(S))