# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):

        last=dummy=ListNode(0)
        dummy.next=l=r=head
        # p(dummy)
        while r:
            count = 0
            while r and count<k:
                count += 1
                r=r.next
            if count==k:
                cur,pre = l, r
                for i in range(k):
                    tmp = cur.next
                    cur.next= pre
                    pre=cur
                    cur=tmp
                last.next = pre
                last = l
                l = r
        return dummy.next

node=head=ListNode(1)
for i in range(2,6):
    node.next = ListNode(i)
    node=node.next
head = Solution().reverseKGroup(head, 2)

while head:
    print(head.val,end=" ")
    head = head.next
