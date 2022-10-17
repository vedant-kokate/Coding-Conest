class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(l,h):
            ans = 0
            while l>=0 and h<n and s[l]==s[h]:
                ans +=1
                l-=1
                h+=1
            return ans
        ans = 0
        n=len(s)
        for i in range(n):            
            ans += count(i,i) + count(i-1,i)
            # print(i,ans)
        return ans
                
s=input().strip()

print(Solution().countSubstrings(s))