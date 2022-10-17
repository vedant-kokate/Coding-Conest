class Solution:
    def decodeString(self, s: str) -> str:
        nums, lett=[], []
        part,number = "",0
        for c in s:
            # print(part)
            # print(nums,lett,part)
            if c=='[':
                nums.append(number)
                lett.append(part)
                part=""
                number = 0
            elif c==']':
                part = lett.pop()+part*nums.pop()
                # print(part)
            elif c.isdigit():
                number = number * 10 + int(c)            
            else:
                part += c
        # print(len(part))
        return part
s=input()
print(Solution().decodeString(s))