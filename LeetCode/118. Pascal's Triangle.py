class Solution:
    def generate(self, n: int) :
        ans=[]
        for i in range(1,n+1):
            ans.append([1]*i)
        
        for i in range(2,n):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        
        for i in ans:
            print(i)
n=4
print(Solution().generate(n))