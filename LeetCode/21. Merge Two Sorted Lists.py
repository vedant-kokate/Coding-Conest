# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        store = ListNode(-100000)
        head = store
        while l1 or l2:
            # print(store.val)
            if not l1:
                v1=10**10
            else:
                v1=l1.val
            if not l2:
                v2=10**10
            else:
                v2=l2.val
            
            if v1<v2:
                temp = ListNode(v1)
                store.next=temp
                store = store.next
                l1 = l1.next
            else:
                temp = ListNode(v2)
                store.next=temp
                store = store.next
                l2 = l2.next
            
        return head.next