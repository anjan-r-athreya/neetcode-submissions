# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headfinal = head
        prev = ListNode(0)
        prev.next = head
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast:
            slow = slow.next
            prev = prev.next
            fast = fast.next
        
        prev.next = slow.next
        return headfinal