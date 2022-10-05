class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            if s[i]==')':
                if stack and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        stack.append(len(s))
        stack.insert(0, -1)
        # print(stack)
        ans=0
        for i in range(1,len(stack)):
            ans = max(ans,stack[i]-stack[i-1]-1)
        return ans

s=input()
print(Solution().longestValidParentheses(s))