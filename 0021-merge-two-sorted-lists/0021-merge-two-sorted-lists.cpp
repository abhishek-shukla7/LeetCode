class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Create a dummy node to start the merged list
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;

        // Loop until either list becomes empty
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                tail->next = list1;  // attach list1 node
                list1 = list1->next; // move list1 forward
            } else {
                tail->next = list2;  // attach list2 node
                list2 = list2->next; // move list2 forward
            }
            tail = tail->next; // move tail forward
        }

        // If any list has remaining nodes, attach them
        if (list1 != nullptr) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }

        return dummy->next; // head of merged list
    }
};
