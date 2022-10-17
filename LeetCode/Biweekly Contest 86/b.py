class Solution:
    def isStrictlyPalindromic(self, n) -> bool:
        def dec_to_base(num,base): 
            base_num = ""
            while num>0:
                dig = int(num%base)
                if dig<10:
                    base_num += str(dig)
                else:
                    base_num += chr(ord('A')+dig-10)  
                num //= base
            base_num
            return base_num==base_num[::-1]
        for base in range(2,n-1):
            if not dec_to_base(n, base):
                return False
        return True


print(Solution().isStrictlyPalindromic(9))