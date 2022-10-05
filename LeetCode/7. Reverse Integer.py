class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if s[0]=='-':
            s=s[1:]
            s=s[::-1]
            s=-int(s)
        else:
            s=s[::-1]
            s=int(s)
        return s if -2**31<=s<2**31 else 0
        