class Solution:
    def f(self,n1,n2,target):
        s1, e1 = 0, len(n1)-1
        
        while s1<e1:
            mid = (s1+e1)//2
            posl = bisect_left(n2,n1[mid])
            posr = bisect_right(n2,n1[mid])
            
            vall = posl + mid
            valr = posr + mid
            if vall<=target<=valr:
                return True,n1[mid]
            elif valr<target:
                s1 = mid + 1
            else:
                e1 = mid
        if s1==e1:
            mid = (s1+e1)//2
            posl = bisect_left(n2,n1[mid])
            posr = bisect_right(n2,n1[mid])
            
            vall = posl + mid
            valr = posr + mid
            if vall<=target<=valr:
                return True,n1[mid]
        return (False,-1)
            
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        n, m = len(n1), len(n2)
        l = (n+m)//2
        r = (n+m-1)//2
        print(l,r)
        t1,v1 = self.f(n1,n2,l)
        print("1",t1,v1)
        if not t1:
            t1,v1 =  self.f(n2,n1,l)
            print("2",t1,v1)
        t1,v2 = self.f(n1,n2,r)
        print("3",t1,v2)
        if not t1:
            t1,v2 =  self.f(n2,n1,r)
            print("4",t1,v2)
            
        return (v1 + v2)/2
        
        
    
        
        