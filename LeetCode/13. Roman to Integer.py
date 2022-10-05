class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        ans = 0
        for i,val in enumerate(s):
            if i+1<len(s) and d[s[i+1]]>d[s[i]]:
                ans-=d[s[i]]
            else:
                ans += d[s[i]]
        return ans
            