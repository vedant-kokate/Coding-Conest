class Solution:
    def dailyTemperatures(self, temp) :
        
        n=len(temp)
        stack =[]
        ans = [0]*n
        for i,val in enumerate(temp):
            if not stack:
                stack.append(i)
            else:
                while stack and temp[stack[-1]]<val:
                    cur = stack.pop()
                    ans[cur] = i-cur
                stack.append(i)
        return ans

temp = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temp))