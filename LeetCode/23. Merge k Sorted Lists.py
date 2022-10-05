# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, l):
        h=[]
        i=0
        for v in l:
            if v:
                heappush(h, (v.val,i,v))
                i+=1
        
#         rhead = rtail = ListNode(0)
        ans = head = ListNode(0)
        while h:
            # print(h)
            i+=1
            v,x, node = heapq.heappop(h)
            head.next=node
            head=head.next
            if head.next:
                heappush(h,(head.next.val,i,head.next))
                
#             rtail.next = n
#             rtail = rtail.next
#             if n.next:
#                 heapq.heappush(h, (n.next.val, i, n.next))
                
        return ans.next


        
            
        