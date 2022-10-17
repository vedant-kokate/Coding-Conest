from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        fr = Counter(s)
        for i,val in enumerate(s):
            if fr[val]==1:
                return i
        return -1            
s=input().strip()
print(Solution().firstUniqChar(s))