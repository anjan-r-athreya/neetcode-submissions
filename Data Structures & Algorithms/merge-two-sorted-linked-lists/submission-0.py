# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head3 = ListNode(0)
        headfinal = head3

        while head1 or head2:
            if not head1:
                head3.next = head2
                break
            elif not head2:
                head3.next = head1
                break
            
            if head1.val <= head2.val:
                head3.next = ListNode(head1.val)
                head3 = head3.next
                head1 = head1.next
            elif head1.val > head2.val:
                head3.next = ListNode(head2.val)
                head3 = head3.next
                head2 = head2.next
        
        return headfinal.next