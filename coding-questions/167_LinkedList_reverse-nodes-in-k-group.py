from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        if type(val) == list:
            self._factory(val)
        else:
            self.val = val
            self.next = next
    
    def __eq__(self, other):
        if type(other) == ListNode and self.val == other.val:
            return self.next == other.next    
        else:
            return False
    
    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + ',' + str(self.next)

    def _factory(self, vals):
        if len(vals) == 0:
            raise ValueError('Constructor given empty list of values')

        self.val = vals[0]
        node = self
        for v in vals[1:]:
            node.next = ListNode(v)
            node = node.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Given:
            head: Head of a LL
            k: Segment side to reverse
                1 <= k, n <= 5000
                0 <= node.val <= 1000
        Return:
            Return head node of the modified list
            * Nodes are immutable (cannot alter values) 

        TIME: O(N)
        SPACE: O(1)
        '''
        if head is None:
            return None

        prev = None
        head0 = head
        i = 0
        # Invariant: Distance between head0 and head is i; `prev` is 1 node before `head`
        while i < k:
            if head is None:
                return head0
            prev = head
            head = head.next
            i += 1

        # head0 ... prev; head
        prev.next = None
        self.reverse(head0)
        node = self.reverseKGroup(head, k)
        head0.next = node
        return prev
        
    def reverse(self, head):
        # Pre: n >= 1
        dummy = ListNode(None, head)
        oldHead = head
        while oldHead.next is not None:
            toMove = oldHead.next
            oldHead.next = toMove.next
            toMove.next = dummy.next
            dummy.next = toMove

        return dummy.next

            




if __name__ == '__main__':
    a_input = ListNode([1,2,3,4,5])
    a_ans = ListNode([2,1,4,3,5])
    b_input = ListNode([1,2,3,4,5])
    b_ans = ListNode([3,2,1,4,5])

    sol = Solution()
    a_res = sol.reverseKGroup(a_input, 2)
    b_res = sol.reverseKGroup(b_input, 3)

    print(a_res)
    print(a_ans)
    print(a_res == a_ans)

    print(b_res)
    print(b_ans)
    print(b_res == b_ans)