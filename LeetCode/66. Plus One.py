class Solution:
    def plusOne(self, a) :
        i=len(a)-1
        while i>=0:
            a[i]+=1
            if a[i]>9:
                # print("hey")
                a[i]=0
                i-=1
            else:
                return a
        a.insert(0,1)
        return a

a=[9]
print(Solution().plusOne(a))