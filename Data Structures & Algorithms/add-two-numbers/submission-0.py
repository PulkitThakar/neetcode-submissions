# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(val=-1)
        curr = dummy

        curr1 = l1
        curr2 = l2
        while curr1 and curr2:
            temp_val = curr1.val + curr2.val + carry
            carry = temp_val // 10
            temp_val = temp_val % 10
            curr.next = ListNode(val=temp_val)
            curr1 = curr1.next
            curr2 = curr2.next
            curr = curr.next
            
        
        while curr1:
            temp_val = curr1.val + carry
            carry = temp_val // 10
            temp_val = temp_val % 10
            curr.next = ListNode(val=temp_val)
            curr1 = curr1.next
            curr = curr.next
        
        while curr2:
            temp_val = curr2.val + carry
            carry = temp_val // 10
            temp_val = temp_val % 10
            curr.next = ListNode(val=temp_val)
            curr2 = curr2.next
            curr = curr.next
        
        while carry:
            temp_val = carry
            carry = temp_val // 10
            temp_val = temp_val % 10
            curr.next = ListNode(val=temp_val)
            curr = curr.next
        
        return dummy.next

            