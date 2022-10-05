class Solution(object):
    def divide(self, dividend, divisor):

        if dividend>2**31-1:
            return 2**31-1
        if dividend<-2**31:
            return -2**31
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i<<1
                temp = temp<<1
        if not positive:
            res = -res
        return min(max(-2**31-1, res), 2**31-1)