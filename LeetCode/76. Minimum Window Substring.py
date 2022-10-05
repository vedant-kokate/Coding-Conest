from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end=0, 0
        f_s=defaultdict(int)
        f_t=defaultdict(int)
        
        for c in t:
            f_t[c] += 1
        ans = [0,len(s),""]
        while end<len(s):
            # print(start,end)
            f_s[s[end]] +=1
            
            while all(f_t[k]<=f_s[k] for k in f_t.keys()):
                # print(s[start:end+1])
                if end-start<ans[1]-ans[0]:
                    ans=[start,end,s[start:end+1]]
                # print(start)
                # ans =[start,end]
                f_s[s[start]] -=1
                start+=1
            end +=1
        
        # print(ans)
        return ans[2]

s = "A"
t = "AA"
print(Solution().minWindow(s, t))