class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        def Add(x, y):

            if (y == 0):
                return x
            else:
                return Add( x ^ y, (x & y) << 1)
        
        def subtract(x, y):
            if (y == 0):
                return x
            return subtract(x ^ y, (~x & y) << 1)
        
        if (a>0 and b>0) or (a<0 and b<0): 
            return Add(a,b)
        elif a<0:
            if abs(a)>abs(b):
                return -subtract(-a, b)
            else:
                return subtract(b, -a)
        else:
            if abs(a)>abs(b):
                return subtract(a, -b)
            else:
                return -subtract(-b, a)

   
a,b = map(int,input().split())
print(Solution().getSum(a, b))