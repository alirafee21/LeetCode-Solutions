/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *turtle = head;
    struct ListNode *rabbit = head;
    while (rabbit != NULL && rabbit->next != NULL)
    {
        turtle = turtle->next;
        rabbit = rabbit->next->next;
        if (turtle == rabbit)
        {
            return true;
        }
    }
    return false;
}