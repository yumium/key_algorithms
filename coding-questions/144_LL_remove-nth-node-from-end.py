# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Given:
            head: Head of linked list
            n: The n-th node from end to remove
                Linked list has at least 1 element
                1 <= n <= size of linked list
        Return:
            Return the head of mutated linked list

        TIME: O(N)
        SPACE: O(1)
        '''
        # Create a dummy node
        head = ListNode(None, head)

        # Find the n-th node
        left = right = head
        for i in range(n-1):
            right = right.next
        
        # Invariant: `right` is (n-1) nodes right of `left`
        while right.next.next is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return head.next
