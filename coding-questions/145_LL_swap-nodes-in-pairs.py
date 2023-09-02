# Source: https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Given:
            head: Head of a linked list
                0 <= size of linked list
        Return:
            Head of linked list where every pairs of adjacent nodes are swapped

        TIME: O(N)
        SPACE: O(1)
        '''
        if head is None:
            return None

        # Create a dummy node
        head = ListNode(None, head)
        head0 = head

        while head.next and head.next.next:
            fst = head.next
            snd = head.next.next

            fst.next = snd.next
            snd.next = fst
            head.next = snd

            head = head.next.next

        # Skip dummy node
        return head0.next
