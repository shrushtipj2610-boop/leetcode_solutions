# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev= None
        current= head
        while current!= None:
            next= current.next
            current.next= prev
            prev= current # move prev forward
            current=next # move current forward
        return prev # as prev is new head of reversed linked list