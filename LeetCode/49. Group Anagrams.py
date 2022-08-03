from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for i in strs:
            temp = "".join(sorted(i))
            d[temp].append(i)
        return d.values()
strs = ["a"]
print(Solution().groupAnagrams(strs))