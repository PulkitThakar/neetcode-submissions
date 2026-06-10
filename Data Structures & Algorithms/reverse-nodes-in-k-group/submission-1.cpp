/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head == nullptr)
            return nullptr;
        
        ListNode* dummy = new ListNode(-1, head);
        
        ListNode* last = head;
        for(int i = 1; i < k and last != nullptr; i++) {
            last = last->next;
        }
        if(last == nullptr)
            return head;

        ListNode* nextPart = last->next;
        last->next = nullptr;

        reverseList(head);

        dummy->next = last;
        head->next = reverseKGroup(nextPart, k);

        return dummy->next;
        
    }

private:
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr)
            return nullptr;
        ListNode* newHead = head;
        if(head->next != nullptr){
            newHead = reverseList(head->next);
            head->next->next = head;
        }
        head->next = nullptr;
        return newHead;
    }
};
