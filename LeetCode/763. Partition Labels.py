class Solution:
    def partitionLabels(self, s: str):
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][1] = i
            else:
                d[s[i]] = [i,i]
                
        r = list(d.values())
        r.sort()
        
        a=[r[0]]
        # print(a)
        for s,e in r:
            if s<a[-1][1] and e>a[-1][1]:
                a[-1][1] = e
            elif s>a[-1][1]:
                # print(s,e,a[-1])
                a.append([s,e])
        ans = []
        for x,y in a:
            ans.append(y-x+1)
        return ans

s=input().strip()

print(Solution().partitionLabels(s))