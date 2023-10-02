# Source: https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Given:
            head: Head of a linked list
                1 <= size <= 5E4
                1 <= node.val <= 1000
        Return:
            None, modify head in-place

        Do not return anything, modify head in-place instead.
        
        TIME: O(N)
        SPACE: O(1)
        """
        if head.next is None:
            return

        head, second = self.split(head)        
        second = self.reverse(second)

        # Traverse through second half and add to first half
        while second:
            if head.next:
                toAdd = second
                second = second.next
                toAdd.next = head.next
                head.next = toAdd
                head = head.next.next
            else:
                head.next = second
                second = second.next

    def split(self, head):
        # Pre: size >= 2
        # Find the head of second half (left biased)
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        return (head, second)

    def reverse(self, head):
        # Pre: size >= 1
        # Reverses linked list in-place and returns new head
        dummy = ListNode(None, head)
        while head.next:
            toMove = head.next
            head.next = toMove.next
            toMove.next = dummy.next
            dummy.next = toMove
        return dummy.next
        