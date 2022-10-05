from collections import Counter as C
from collections import deque
class Solution:
    def ladderLength(self, b: str, e: str, w) -> int:
             
        n=len(w)
        d = {}
        for word in w:
            d[word]=True

        stack=deque([(b,1)])
        while stack:
            cur,l=stack.popleft()
            if cur==e:
                # print(vis)
                return l
            
            for i in range(len(cur)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = cur[:i] + c + cur[i+1:]
                    if new_word in d:
                        
                        stack.append((new_word,l+1))
                        del d[new_word]

        return 0
                        
        
      
# "leet"
# "code"          
b="leet"
e="code"
w=["lest","leet","lose","code","lode","robe","lost"]
print(Solution().ladderLength(b, e, w))