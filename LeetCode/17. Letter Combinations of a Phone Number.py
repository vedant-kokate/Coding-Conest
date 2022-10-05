class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        
        m={'2':['a','b','c'],
           '3':['d','e','f'],
           '4':['g','h','i'],
           '5':['j','k','l'],
           '6':['m','n','o'],
           '7':['p','q','r','s'],
           '8':['t','u','v'],
           '9':['w','x','y','z'],
          }
        
        ans = deque()
        if len(d)==0:
            return []
        for x in m[d[0]]:
            ans.append(x)
        while True:
            cur = ans.popleft()
            pos = len(cur)
            if pos==len(d):
                ans.append(cur)
                break
            
            for x in m[d[pos]]:
                ans.append(cur+x)
        return ans
            
            