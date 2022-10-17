class Solution:
    def maxSatisfaction(self, a) :
        n=len(a)
        a.sort()
        ans = 0
        for i in range(n):
            s = 0
            for j in range(n-i):
                s += (j+1)*a[i+j]
            ans = max(ans,s)
        print(ans)
                


Input = list(map(int,input().split()))
Solution().maxSatisfaction(Input)