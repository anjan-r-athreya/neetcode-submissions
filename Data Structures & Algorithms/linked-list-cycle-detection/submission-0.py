# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyds tortoise and hare algo
        slow = head
        fast = head

        while slow and fast:
            if not fast or not fast.next or not fast.next.next or not slow or not slow.next:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False