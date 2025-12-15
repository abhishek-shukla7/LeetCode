# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node=ListNode(0)
        node.next=head

        a=node
        b=node

        for _ in range(n):
            a=a.next

        while a.next:
            a=a.next
            b=b.next

        b.next=b.next.next
        return node.next

        
        