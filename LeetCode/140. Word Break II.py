class Solution:
    def wordBreak(self, s: str, wordDict):
        def f(word,l):
            if word=="":
                self.ans.append(" ".join(l))
            for i in range(1,len(word)+1):
                w = word[:i]
                if w in d:
                    f(word[i:],l+[w])
        self.ans = []
        d={}
        for word in wordDict:
            d[word] = True
        f(s,[])
        return self.ans

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))