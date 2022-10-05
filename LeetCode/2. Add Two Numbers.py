# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def l_to_int(l):
            ans=""
            while l is not None:
                ans+=str(l.val)
                l=l.next
            return int(ans[::-1])
        ans=str(l_to_int(l1)+l_to_int(l2))[::-1]
        head=ListNode(int(ans[0]))
        store =head
        
        print(ans)
        for i in range(1,len(ans)):
            head.next = ListNode(int(ans[i]))
            head=head.next
        return store
                
                
        