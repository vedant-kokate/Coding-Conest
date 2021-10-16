
for _ in range(int(input())):
    s1=input().strip()
    s2=input().strip()
    n=len(s1)
    k=len(s2)
    ans = 10**10
    for i in range(n - k + 1):
         ss = s1[i:i+k]
         ans = min(ans, sum(ss[j]!=s2[j] for j in range(k)))
    print(ans)
