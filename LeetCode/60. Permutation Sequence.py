class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        dig = list(range(1,n+1))
        
        ans = ""
        f=[1]*(n+1)
        for i in range(1,n+1):
            f[i] = i*f[i-1]
        
        k-=1
        
        while dig:
            n-=1
            idx = k//f[n]
            ans+=str(dig[idx])
            del  dig[idx]
            
            k%=f[n]
            
        return ans
            