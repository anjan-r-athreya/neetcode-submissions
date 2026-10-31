# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

        
"""
prev, current, next
sentinel -> start
next = start.next
current.next = prev
prev = current
current = next
while current != None
"""