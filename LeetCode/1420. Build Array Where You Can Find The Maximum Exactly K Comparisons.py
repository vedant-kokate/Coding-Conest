class Solution:
    def numOfArrays(self, n, m, k):

        def f(idx, max_till_now, k):
            if (idx,max_till_now,k) in self.mem:
                return self.mem[(idx,max_till_now,k)]
            if n-idx<k:
                return 0
            if idx==n and k==0:
                return 1

            ans = 0
            for i in range(max_till_now+1,m+1):
                ans += f(idx + 1, i, k-1)

            ans +=  f(idx + 1, max_till_now,k)*max_till_now
            ans%=mod

            self.mem[(idx,max_till_now,k)] = ans
            return ans
        
        self.mem = {}
        mod = 10**9+7
        
        if m<k:
            return 0
        return(f(0,0,k)%mod)
            
        
n,m,k = map(int,input().split())
print(Solution().numOfArrays(n, m, k))