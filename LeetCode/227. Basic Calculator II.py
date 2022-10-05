class Solution:
    def calculate(self, s: str) -> int:
        a=[]
        num = 0
        sign = '+'
        s +='+'
        for c in s:
            # print(a)
            if c.isdigit():
                num = num*10 + int(c)
            elif c in ['+','-','*','/']:
                if sign=='+':
                    a.append(num)
                elif sign=='-':
                    a.append(-num)
                elif sign=='*':
                    a.append(a.pop()*num)
                else:
                    x=a.pop()
                    if x//num<0 and x%num!=0:
                        a.append(x//num+1)
                    else:
                        a.append(x//num)
                sign =c
                num=0
        
        a.append(num)
        # print(a)
        return sum(a)
        
s = input()
print(Solution().calculate(s))