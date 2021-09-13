class Solution:
    def solve(self, n, x, y, k):
        mem={}
        def calc_prob(i, j, step, prob):
            
            if not(1<=i<=n and 1<=j<=n):
                return 0
            # print(i,j,step,prob)
            if step==k:
                return prob
            if (i,j,step) in mem:
                return mem[(i,j,step)]
          
            p=calc_prob(i+2,j+1,step+1,prob/8) + calc_prob(i+2,j-1,step+1,prob/8) 
            p+=calc_prob(i+1,j+2,step+1,prob/8) + calc_prob(i+1,j-2,step+1,prob/8) 
            p+=calc_prob(i-2,j+1,step+1,prob/8) + calc_prob(i-2,j-1,step+1,prob/8) 
            p+=calc_prob(i-1,j+2,step+1,prob/8) + calc_prob(i-1,j-2,step+1,prob/8) 
          
            mem[(i,j,step)]=p
            return p
        ans=calc_prob(x+1,y+1,0,1)*100
        # print(mem)
        return int(ans)