# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_sorted_lists(self, l1, l2):
        dummy = ListNode(val = -1, next = None)
        curr = dummy
        while l1 and l2:
            temp = ListNode()
            if l1.val < l2.val:
                temp.val = l1.val
                l1 = l1.next
            else:
                temp.val = l2.val
                l2 = l2.next
            curr.next = temp
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr_lists = lists
        while len(curr_lists) > 1:
            next_lists = [
                self.merge_sorted_lists(curr_lists[2*i], curr_lists[2*i + 1]) for i in range(len(curr_lists) // 2)
            ]
            if len(curr_lists) % 2:
                next_lists.append(curr_lists[-1])
            
            curr_lists = next_lists
        
        return None if not curr_lists else curr_lists[0]