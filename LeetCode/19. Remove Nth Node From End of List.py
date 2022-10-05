# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        store = head
        l=0
        while head:
            head=head.next
            l+=1
        head = store
        
        cur =0
        pos = l-n-1
        if pos==-1:
            return store.next
        while head:
            if cur==pos:
                head.next=head.next.next
                break
            head=head.next
            cur+=1
        return store