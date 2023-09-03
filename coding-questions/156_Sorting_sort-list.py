# https://leetcode.com/problems/sort-list/submissions/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Given:
            head: Head of linked list
                0 <= size of linked list <= 5E4
                -1E5 <= Node.val <= 1E5
        Return:
            Head of list with elements sorted in ascending order

        TIME: O(N log N)
        SPACE: O(N)
        '''
        if head is None or head.next is None:
            return head

        # At least 2 elements
        mid = self.findMiddle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeList(left, right)

    def mergeList(self, left, right):
        '''
        Merge lists `left` and `right`, return head of merged list
            1 <= size(left), size(right)
        '''
        res = res0 = ListNode(None, None)
        while left is not None:
            if right is None or left.val <= right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        
        if right is not None:
            res.next = right
        
        return res0.next

    
    def findMiddle(self, head):
        '''
        Find middle of `head`, break into 2 lists, and return head of 2nd list
            2 <= size(head)
        '''
        slow = head
        fast = head.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        res = slow.next
        slow.next = None
        return res