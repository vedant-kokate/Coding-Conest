class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        ans = 0
        start = 0
        i = 0
        while i <len(s):
            ans = max(ans,i-start)
            if s[i] in d:                
                start = max(d[s[i]]+1,start)
            d[s[i]] = i
            i+=1
        return max(ans,i-start)