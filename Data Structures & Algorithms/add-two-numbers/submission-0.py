# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        head = l3
        carry = 0

        while l2 or l1 or carry:
            current = 0

            if l2 and l1: current += l1.val + l2.val
            elif l2 and not l1: current += l2.val
            elif l1 and not l2: current += l1.val

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            current += carry

            if current >= 10: # there is a remainder
                l3.next = ListNode(current % 10)
                carry = current // 10
            else: # there is no remainder
                l3.next = ListNode(current)
                carry = 0
            
            l3 = l3.next
        
        return head.next