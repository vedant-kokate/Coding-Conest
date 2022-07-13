class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        for i,val in enumerate(s):
            if i==0 and (val=='+' or val=='-'):
                continue
            if not val.isdigit():
                s=s[:i]
                break
        if s=="" or s=='+' or s=='-':
            return 0
        s=int(s)
        if s>2**31-1:
            s=2**31-1
        if s<-1*2**31:
            s=-1*2**31
        return s
print(Solution().myAtoi("+-12"))