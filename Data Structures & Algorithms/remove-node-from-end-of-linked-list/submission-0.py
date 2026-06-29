# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        head1 = head
        finalhead = head
        
        while head:
            head = head.next
            length += 1

        if n == length:
            return head1.next
        
        iterations = length - n

        prev = ListNode(0)
        prev.next = head1

        for i in range(iterations):
            head1 = head1.next
            prev = prev.next
        
        prev.next = head1.next
        return finalhead