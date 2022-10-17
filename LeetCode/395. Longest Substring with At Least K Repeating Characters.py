from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def f(s):
            for c in set(s):
                if s.count(c)<k:
                    m=0
                    for substring in s.split(c):
                        m=max(f(substring),m)
                    return m
            return len(s)
        return f(s)
        # for c in set(s):
        #     if s.count(c) < k:
        #         return max(self.longestSubstring(t, k) for t in s.split(c))
        # return len(s)




s=input()
k=int(input())
print(Solution().longestSubstring(s, k))