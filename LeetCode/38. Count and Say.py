class Solution:
    def countAndSay(self, n: int) -> str:
        def f(s):
            last = "*"
            count = 1
            ans = ""
            for i in s:
                # print(last,count,i)
                if i==last:
                    count+=1
                else:
                    ans += str(count)+last
                    # print(ans,'ans')
                    last = i
                    count = 1
            ans += str(count)+last 
            return ans[2:]
        Ans = "1"
        for i in range(n-1):
            Ans = f(Ans)
        return Ans
                    
                    
n=int(input())
print(Solution().countAndSay(n))