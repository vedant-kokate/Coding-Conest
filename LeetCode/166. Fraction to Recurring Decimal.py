from collections import defaultdict
class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        sign = '-' if n*d < 0 else ''
        n,d=abs(n),abs(d)     
        div,rem=divmod(n, d)
        res = [sign+str(div), '.']
        r={}
        while rem!=0 and rem not in r:
            r[rem] = len(res)
            div,rem=divmod(rem*10,d)
            res.append(str(div))
        if rem in r:
            res.insert(r[rem], '(')
            res.append(')')
        # print(res)
        return "".join(res).strip(".")
n=int(input())
d=int(input())
print(Solution().fractionToDecimal(n, d))
