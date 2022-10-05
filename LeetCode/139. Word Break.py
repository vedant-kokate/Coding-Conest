from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        n=len(s)
        dp = [1]+[0]*n
        for i in range(n):
            if dp[i]:
                for j in range(i+1,n+1):
                    if s[i:j] in wordDict:
                        dp[j] = 1
        return dp[-1]==1


        

       

s="leetcode"
wordDict = ["leet","code"]

print(Solution().wordBreak(s, wordDict))