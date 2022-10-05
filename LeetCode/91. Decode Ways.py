class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp = [1,1] + [0]*(n-1)
        if s[0]=='0':
            return 0
        
        for i in range(2,n+1):
            if int(s[i-1])>0:
                dp[i] += dp[i-1]
            if 9<int(s[i-2:i])<27:
                dp[i] += dp[i-2]
            
        return dp[-1]
            

s = input()       
print(Solution().numDecodings(s))