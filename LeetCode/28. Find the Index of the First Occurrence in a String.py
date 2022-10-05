class Solution:
    def strStr(self, h: str, n: str) -> int:
        i,j=0,0
        while i<len(h) and j<len(n):
            if h[i]==n[j]:
                i+=1
                j+=1
            else:
                i -=j-1
                j=0
        if j==len(n):
            return i-j
        else: return -1