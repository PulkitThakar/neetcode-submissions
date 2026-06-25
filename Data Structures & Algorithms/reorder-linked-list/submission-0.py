# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        
        if not fast:
            return
        
        while(slow.next and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        toReverse = None
        if not fast.next:
            toReverse = slow.next
            slow.next = None
        else:
            toReverse = slow.next.next
            slow.next.next = None
        
        toReverse = self.reverseList(toReverse)
        curr = head
        while(toReverse):
            temp = curr.next
            
            curr.next = toReverse
            toReverse = toReverse.next
            
            curr.next.next = temp
            curr = curr.next.next
    
    def reverseList(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
