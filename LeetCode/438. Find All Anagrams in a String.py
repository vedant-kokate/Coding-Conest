from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str):
        f_p=defaultdict(int)
        f_s=defaultdict(int)
        n,m = len(s),len(p)
        for i in range(26):
            f_s[chr(97+i)] =0
            f_p[chr(97+i)] =0
        for c in p:f_p[c] += 1
        
        for i in range(m):
            f_s[s[i]] += 1
            
        res = []
        if f_p==f_s:
            res.append(0)
        print(m,n)
        for i in range(m,n):
            f_s[s[i]] +=1
            f_s[s[i-m]] -=1
            # print(f_s)
            if f_p==f_s:
                res.append(i-m+1)
        return res

s=input()
p=input()
print(Solution().findAnagrams(s, p))