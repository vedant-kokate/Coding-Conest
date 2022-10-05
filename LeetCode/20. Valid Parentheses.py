class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if i==']' and stack and stack[-1]=='[':
                    stack.pop()
                elif i=='}' and stack and stack[-1]=='{':
                    stack.pop()
                elif i==')' and stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            # print(stack)
        return stack==[]
                    