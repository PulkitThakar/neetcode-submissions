# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        curr = dummy

        carry = 0
        while l1 or l2:
            s = 0 if not l1 else l1.val
            s = s + (0 if not l2 else l2.val)
            s = s + carry
            carry = s // 10
            s = s % 10
            curr.next = ListNode(s, None)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry, None)
        
        return dummy.next