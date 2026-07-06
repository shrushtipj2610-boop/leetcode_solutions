# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None:
            return None
        current= head
        runner= head
        while runner != None and runner.next != None:
            current= current.next
            runner= runner.next.next 
        prev= None
        while current is not None:
            next= current.next
            current.next= prev
            prev= current
            current= next
        max_sum = 0
        first = head
        second = prev
        while second is not None:
            max_sum = max (max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum
        